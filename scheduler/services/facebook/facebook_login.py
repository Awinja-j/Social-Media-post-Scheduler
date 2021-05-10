import os
import urllib
import json
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import LongLivedAccessToken
from .serializers import LongLivedAccessTokenSerializers

class FacebookLoginFlow(APIView):

    def __init__(self):
        self.user_access_token=os.environ['facebook_short_time_user_access_token']
        self.graph_endpoint="https://graph.facebook.com/"
        self.app_id=os.environ['facebook_app_id']
        self.app_secret=os.environ['facebook_app_secret']
        self.graph_api_version="v10.0"

    def generate_user_access_token(self):
        pass
        # token=""
        # self.user_access_token=token

    def get(self, request, format=None):
        """
        generate_long_lived_access_token
        Calls oauth/access_token endpoint
        Sample response: 
        {
        "access_token":"{long-lived-user-access-token}",
        "token_type": "bearer",
        "expires_in": 5183944 //The number of seconds until the token expires
        }
        """
        url = '{}{}{}{}{}{}{}{}{}{}'.format(self.graph_endpoint, self.graph_api_version, '/oauth/access_token?','grant_type=fb_exchange_token&', 'client_id=', self.app_id, \
                '&client_secret=', self.app_secret, '&fb_exchange_token=', self.user_access_token)

        
        with urllib.request.urlopen(url) as response:
                long_lived_access_token = response.read().decode('utf-8')
        data = json.loads(long_lived_access_token)
        access_token=data['access_token']
        toke_type=data['token_type']
        expires_in=data['expires_in']

        #TODO: Send data to db

    def post(self, request, format=None):
        """
        post to facebook
        """
        try:
            print('joy')
        except:
            print('no joy')

class FacebookPagePosts(APIView):
    def __init__(self):
        pass
    def get(self):
        pass
    def post(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass



class FacebookCallback(APIView):

    def __init__(self):
        pass

    def get(self, request, format=None):
        pass