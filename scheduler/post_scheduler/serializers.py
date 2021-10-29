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

   

