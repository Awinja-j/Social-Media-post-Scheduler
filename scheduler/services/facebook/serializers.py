from rest_framework import serializers
from .models import LongLivedAccessToken

class LongLivedAccessTokenSerializers(serializers.Serializer):
    access_token = serializers.CharField(max_length=500)
    token_type = serializers.CharField(max_length=500)
    expires_in = serializers.DateTimeField()
    date_created = serializers.DateTimeField()

    def create(self, validated_data):
        return LongLivedAccessToken.objects.get_or_create(**validated_data)

    def update(self, instance, validated_data):
        instance.access_token = validated_data.get('access_token', instance.access_token)
        instance.token_type = validated_data.get('token_type', instance.token_type)
        instance.expires_in = validated_data.get('expires_in', instance.expires_in)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.save()
        return instance