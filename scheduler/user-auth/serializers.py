from rest_framework import serializers 
from .models import  Posts

class PostsSerializer(serializers.ModelSerializer):
    photo_id=serializers.CharField(max_length=11)
    photo_url=serializers.CharField(max_length=255) 
    post_caption=serializers.CharField(max_length=5000, allow_blank=True, allow_null=True)
    is_published=serializers.BooleanField(default=False)
    is_twitter=serializers.BooleanField(default=False)
    is_facebook=serializers.BooleanField(default=False)
    is_linkedin=serializers.BooleanField(default=False)
    datetime_to_publish=serializers.DateField()

    class Meta:
        model = Posts
        fields = '__all__'

    def create(self, validated_data):
        return Posts.objects.get_or_create(**validated_data)

    def update(self, instance, validated_data):
        instance.photo_id=validated_data.get('photo_id', instance.photo_id)
        instance.photo_url= validated_data.get('photo_url', instance.photo_url)
        instance.post_caption=validated_data.get('post_caption', instance.post_caption)
        instance.is_published=validated_data.get('is_published', instance.is_published)
        instance.is_twitter=validated_data.get('is_twitter', instance.is_twitter)
        instance.is_facebook=validated_data.get('is_facebook', instance.is_facebook)
        instance.is_linkedin=validated_data.get('is_linkedin', instance.is_linkedin)
        instance.datetime_to_publish=validated_data.get('datetime_to_publish', instance.datetime_to_publish)
        instance.save()
        return instance
   

