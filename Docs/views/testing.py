from rest_framework.views import APIView
from rest_framework.response import Response


class CheckView(APIView):
    def get(self, request):
        print("yo nigga")

        return Response("I think this is working", headers={
            "Access-Control-Allow-Origin": "http://localhost:3000/"
        }, )