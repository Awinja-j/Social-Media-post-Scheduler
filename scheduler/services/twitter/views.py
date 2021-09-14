import requests
import os
import json
from rest_framework.response import Response
''''
actions performed by this intergrations include:
- update status
     endpoint: POST statuses/update
- delete status
    endpoint: POST statuses/destroy/:id
- get followers
    endpoint: 
- get all your tweets
    endpoint: 
'''
class TwitterIntergration:
    def __init__(self):
        self.bearer_token = os.environ.get("twitter_bearer_token")
        self.user_id = os.environ.get("twitter_user_id")
        self.twitter_version = os.environ.get("twitter_api_version")

    allowed_methods = {
        'GET'
        'POSt'

    }
    
    def create_url(self, version, endpoint_pattern):
        user_id = self.bearer_token
        return "https://api.twitter.com/2/users/{}/tweets".format(user_id)


    def get_params(self):
        # Tweet fields are adjustable.
        # Options include:
        # attachments, author_id, context_annotations,
        # conversation_id, created_at, entities, geo, id,
        # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
        # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
        # source, text, and withheld
        return {"tweet.fields": "created_at"}


    def create_headers(self, bearer_token):
        headers = {"Authorization": "Bearer {}".format(bearer_token)}
        return headers


    def connect_to_endpoint(self, url, headers, params, method):
        if method not in self.allowed_methods:
            return Response({'status_code':400})

        response = requests.request(method, url, headers=headers, params=params)
        if response.status_code != 200:
            raise Exception(
                "Request returned an error: {} {}".format(
                    response.status_code, response.text
                )
            )
        return response.json()

    def main(self, method):
        url = self.create_url()
        headers = self.create_headers(self.bearer_token)
        params = self.get_params()
        json_response = self.connect_to_endpoint(url, headers, params, method)
        print(json.dumps(json_response, indent=4, sort_keys=True))

