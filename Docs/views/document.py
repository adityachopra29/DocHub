from rest_framework import viewsets
from Docs.models.document import Document
from Docs.models.user import User
from rest_framework import authentication, permissions, parsers
from Docs import serializers
from Docs.models import access_permissions
from rest_framework.response import Response


class DocumentViewSet(viewsets.ModelViewSet):
    queryset=Document.objects.all()
    serializer_class = serializers.DocumentSerializer
    authentication_classes=[authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


    def list(self, request):
        # need to see from perission database that user has the permission to access the doc
        try:
            print("we in guys")
            user = request.user
            doc_list = Document.objects.filter(owner = user)
            serializer = serializers.DocumentSerializer(doc_list, many = True)
            print(doc_list)
            return Response(serializer.data)
            
        except Exception as error:
            print(error)
            return Response("Error in list view")
        
    def retrieve(self, request, *args, **kwargs):
        user = request.user
        id = kwargs.get('pk')
        doc = Document.objects.get(id = id)
        serializer = serializers.DocumentSerializer(doc)
        print(doc.owner)
        print(user)
        if doc.owner != user:
            return Response("this not")
        else:
            print(doc)
            serializer = serializers.DocumentSerializer(doc)
            return Response(serializer.data)