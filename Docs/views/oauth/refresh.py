import os
from rest_framework import views
import requests


# does not do anything right now
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = 'http://localhost:8000/home/'
success_string1 = 'yay'
request_url = 'https://channeli.in/open_auth/token/'

refresh_params = {'client_id': client_id,
        'client_secret': client_secret, 
        'grant_type': 'refresh_token',
        'code': '' ,
        'redirect_uri' : redirect_uri,
        'state': success_string1}


class Refresh_Token(views.APIView):
    r = requests.post(url=request_url, data=refresh_params)