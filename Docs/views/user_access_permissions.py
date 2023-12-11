from rest_framework import viewsets
from Docs.models import user
from Docs.models import access_permissions
from Docs import serializers
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from ..session_auth import CsrfExemptSessionAuthentication
from rest_framework import authentication, permissions, parsers



@method_decorator(csrf_exempt, name='dispatch')
class UserPermissionViewSet(viewsets.ModelViewSet):
    queryset=access_permissions.UserAccess.objects.all()
    serializer_class = serializers.access_permissions.UserPermissionsSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, authentication.BasicAuthentication)
    permission_classes = [permissions.IsAuthenticated]

    # when a user tries to find all the documents where he has some permissions and classifies if it is personal document or shared document by scanning for more entries containing that doc
    def list(self, request, *args, **kwargs):
        print("we in retreive mode")
        user = request.user
        print(user)
        # try:
        docs_with_permissions_list  = access_permissions.UserAccess.objects.filter(for_user = user)
        response_list = []
        for entry in docs_with_permissions_list:
            doc_serializer = serializers.DocumentSerializer(entry.document)
            users_with_permission_count = access_permissions.UserAccess.objects.filter(document = entry.document).count()
            print(users_with_permission_count)
            if users_with_permission_count > 1:
                is_personal = False
            else:
                is_personal = True
            permission_level = entry.permission_level
            response_list.append([doc_serializer.data, permission_level, is_personal])
        print(response_list)
        return Response(response_list)

        # except Exception as e :
        #     print("There was some error in access permissions: ", e)
        #     return Response("error in list of user access: ")

        