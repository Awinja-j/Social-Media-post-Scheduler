from .models import Posts
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostsSerializer
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import shortuuid
import schedule
import time

ps=PostsSerializer()

@api_view(['GET'])
def get_posts(request):
    '''
    display all posts associated with the user
    '''
    posts = Posts.objects.all()
    serializer=PostsSerializer(posts, many=True)
    return Response({"posts": serializer.data})

@api_view(['GET'])
def get_post(request, pk):
    '''
    get a single post associated with the user
    '''
    post = Posts.objects.get(pk=pk)
    serializer=PostsSerializer(post)
    return Response({"post": serializer.data})

@api_view(['GET'])
def search_for_a_post():
    # To Do
    pass

@api_view(['POST'])
def post_posts(request):
    '''
    post a post to the user account| data in json body
    '''
    data={
        'photo_id':shortuuid.uuid()[11:],
        'photo_url':request.data.get("photo_url"),
        'post_caption':request.data.get("post_caption"),
        'is_published':False,
        'is_twitter':request.data.get("is_twitter"),
        'is_facebook':request.data.get("is_facebook"),
        'is_linkedin':request.data.get("is_linkedin"),
        'datetime_to_publish':request.data.get("datetime_to_publish") #It must be in YYYY-MM-DD format.
    }
    try:
        serializer=ps.create(data)
        return Response({"message":"post saved succesfully"})
    except:
        return Response({"message": "error"})


@api_view(['DELETE'])
def delete_post(request, pk):
    '''
    delete a post associated with the user
    '''
    post=get_object_or_404(Post.objects.all(), pk=pk)
    post.delete()
    return Response({"message": "Post deleted Succefully"})

@api_view(['PUT'])
def edit_post(request, pk):
    '''
    edit a post associated with the user
    '''
    post=get_object_or_404(Post.objects.all(), pk=pk)
    data = {
        'photo_id':shortuuid.uuid()[11:],
        'photo_url':request.data.get("photo_url"),
        'post_caption':request.data.get("post_caption"),
        'is_published':False,
        'is_twitter':request.data.get("is_twitter"),
        'is_facebook':request.data.get("is_facebook"),
        'is_linkedin':request.data.get("is_linkedin"),
        'datetime_to_publish':request.data.get("datetime_to_publish") #It must be in YYYY-MM-DD format.
    }
    serilaizer=PostsSerializer(instance=data, data=data, partial=True)
    if serializer.is_valid(raise_exception=True):
        post_saved = serilaizer.save()
    return Response({"message": "Post updated succesfully"})

def schedule_engine(time, function_to_call):
    '''
    This function utilizes the python schedule package to call functions when required
    '''
    pass