from rest_framework import viewsets
from Docs.models.document import Document
from Docs.models.user import User
from rest_framework import authentication, permissions, parsers, status
from Docs import serializers
from Docs.models.access_permissions import UserAccess
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from ..session_auth import CsrfExemptSessionAuthentication

@method_decorator(csrf_exempt, name='dispatch')
class DocumentViewSet(viewsets.ModelViewSet):
    queryset=Document.objects.all()
    serializer_class = serializers.DocumentSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, authentication.BasicAuthentication)
    permission_classes = [permissions.IsAuthenticated]

        
    # def list(self, request):
    #     # need to see from perission database that user has the permission to access the doc
    #     try:
    #         print("we in document list mode")
    #         user = request.user  #here the user is the session authentication wala abstract user
    #         doc_list = Document.objects.filter(owner = user)
    #         serializer = serializers.DocumentSerializer(doc_list, many = True)
    #         # print(doc_list)
    #         return Response(serializer.data)
            
    #     except Exception as error:
    #         print(error)
    #         return Response("Error in list view")
    def list(self, request):
        pass

    def partial_update(self, request, *args, **kwargs):
        print("this is edit")
        user = request.user
        id = kwargs.get('pk')
        document = Document.objects.get(id = id)
        try:
            permissions = UserAccess.objects.get(document = document, for_user = user)
            if permissions.permission_level >= 3:
                # user has the permissions
                print("permission there")
                data = request.data    
                serializer = serializers.DocumentSerializer(instance=document, data=request.data)      
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(serializer.error_messages) 
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)     
        except UserAccess.DoesNotExist:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


    def retrieve(self, request, *args, **kwargs):
        print("This is retreive")
        user = request.user
        print(user)
        id = kwargs.get('pk')
        try:
            doc = Document.objects.get(id = id)
            serializer = serializers.DocumentSerializer(doc)
            # print(doc.owner)
            # print(user)
            permissions = UserAccess.objects.get(document = doc, for_user = user)
            if not permissions:
                return Response("No access")
            else:
                print(doc)
                serializer = serializers.DocumentSerializer(doc)
                return Response(serializer.data)
        except:
            return Response("The doc doesnt exist")

    def destroy(self, request, *args, **kwargs):
        print("we deleting the document")
        user = request.user
        id = kwargs.get('pk')
        document = Document.objects.get(id = id)
        try:
            permission = UserAccess.objects.get(for_user = user, document = document)
            if permission.permission_level != 4:
                return Response("User does not have delete access")
        except UserAccess.DoesNotExist:
            # User has no access to the document
            print("User has no access to the document")
            return Response("User has no access to the document")
        except Exception as e:
            return Response(e)
        document.delete()
        return Response("Successfully deleted document")
    
    
    def create(self, request):
        print("We in document create view")
        user = request.user
        # print(request.data)
        document = Document.objects.create(
            owner = user,
            name = request.data['name'],
            delta = {},
        )
        document_serializer = serializers.DocumentSerializer(document)
        print("document created: ", document_serializer.data)
        UserAccess.objects.create(
            document = document,
            for_user = user,
            permission_level = 4
        )
        print("gave delete access to the user(owner): ", user)


        print(request.data)

        # for delete
        try:
            delete_permissions_list = request.data['delete_permissions']
            for entry in delete_permissions_list:
                if(entry == ''):
                    # print("blanck aagaya so continuing")
                    continue
                try:
                    for_user = User.objects.get(tag = entry)
                    UserAccess.objects.create(
                        document = document,
                        for_user =for_user,
                        permission_level = 4
                    )
                    print("Created delete access for user", entry)
                except Exception as e:
                    print("Failed to add delete access for user with tag: ", entry)

        except Exception as e:
            print("delete permission error: " , e) 

        # for write
        try:
            write_permissions_list = request.data['write_permissions']
            for entry in write_permissions_list:
                if(entry == ''):
                    # print("blanck aagaya so continuing")
                    continue
                try:
                    for_user = User.objects.get(tag = entry)
                    UserAccess.objects.create(
                        document = document,
                        for_user =for_user,
                        permission_level = 3
                    )
                    print("Created write access for user", entry)
                except Exception as e:
                    print("Failed to add write access for user with tag: ", entry)
        except Exception as e:
            print("write permission error: " , e)

        
        # for comment
        try:
            comment_permissions_list = request.data['comment_permissions']
            
            for entry in comment_permissions_list:
                if(entry == ''):
                    # print("blanck aagaya so continuing")
                    continue
                try:
                    for_user = User.objects.get(tag = entry)
                    UserAccess.objects.create(
                        document = document,
                        for_user =for_user,
                        permission_level = 2
                    )
                    print("Created comment access for user", entry)
                except Exception as e:
                    print("Failed to add comment access for user with tag: ", entry)
        except Exception as e:
            print("comment permission error: " , e)
        

        # for read
        try:
            read_permissions_list = request.data['read_permissions']
            for entry in read_permissions_list:
                if(entry == ''):
                    # print("blanck aagaya so continuing")
                    continue
                try:
                    for_user = User.objects.get(tag = entry)
                    UserAccess.objects.create(
                        document = document,
                        for_user = for_user,
                        permission_level = 1
                    )
                    print("Created read access for user", entry)
                except Exception as e:
                    print("Failed to add read access for user with tag: ", entry, e)
        except Exception as e:
            print("read permission error: " , e)

        return Response(document_serializer.data)
        
        