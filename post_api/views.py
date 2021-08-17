from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post

# Create your views here.

# Get all post


@api_view(['GET'])
def index(request):
    try:
        allPosts = Post.objects.all()
        serializer = PostSerializer(allPosts, many=True)
        return Response(serializer.data)
    except:
        Response('Something went wrong',
                 status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Create a new post


@api_view(['POST'])
def create(request):
    try:
        title = request.data['title']
        body = request.data['body']
        isPublish = request.data['isPublish']
        # check is post exist
        poste = Post.objects.get(title=title)
        if poste:
            return Response('Post already exist', status=status.HTTP_409_CONFLICT)

        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    except:
        Response('Something went wrong',
                 status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Update a new post


@api_view(['PUT'])
def update(request, postId):
    try:
        post = Post.objects.get(id=postId)
        serializer = PostSerializer(instance=post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    except:
        Response('Something went wrong',
                 status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Get a single post


@api_view(['GET'])
def fetchPost(request, postId):
    try:
        post = Post.objects.get(id=postId)
        serializer = PostSerializer(post, many=False)
        return Response(serializer.data,)
    except:
        return Response('Post not found', status=status.HTTP_404_NOT_FOUND)

# Delete a post


@api_view(['DELETE'])
def deletePost(request, postId):
    try:
        post = Post.objects.get(id=postId)
        post.delete()
        return Response(data='Post deleted', status=status.HTTP_200_OK)
    except:
        return Response('Post not found', status=status.HTTP_404_NOT_FOUND)
