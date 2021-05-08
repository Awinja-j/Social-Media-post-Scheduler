from .models import Posts
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostsSerializer
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import shortuuid
import os
import http.client

    
class UserAuth:
    def __init__:
        pass

    def auth_connect(self):
        """Response
        {
        "access_token": "soemthing",
        "token_type": "Bearer"
        }
        """

        conn = http.client.HTTPSConnection("lab-ingari.us.auth0.com")
        client_id=os.environ['client_id']
        client_secret=os.environ['client_secret']
        audiance=os.environ['audiance']
        grant_type=os.environ['grant_type']

        payload = "{\"client_id\":client_id,\"audience\":\"https://lab-ingari.us.auth0.com/api/v2/\",\"grant_type\":\"client_credentials\"}"

        headers = { 'content-type': "application/json" }

        conn.request("POST", "/oauth/token", payload, headers)

        res = conn.getresponse()
        data = res.read()

        return data.decode("utf-8")

    def login(self):
        pass

    def logout(self):
        pass
    
    def forgot_password(self):
        pass

