from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post
# Create your views here.


@api_view(['GET'])
def index(request):
    try:
        allPosts = Post.objects.all()
        serializer = PostSerializer(allPosts, many=True)
        return Response(serializer.data,)
    except:
        Response('Something went wrong', status=500)


@api_view(['POST'])
def create(request):
    try:
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
    except:
        Response('Something went wrong', status=500)


@api_view(['PUT'])
def update(request, postId):
    try:
        post = Post.objects.get(id=postId)
        serializer = PostSerializer(instance=post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
    except:
        Response('Something went wrong', status=500)


@api_view(['GET'])
def fetchPost(request, postId):
    try:
        post = Post.objects.get(id=postId)
        serializer = PostSerializer(post, many=False)
        return Response(serializer.data,)
    except:
        return Response('Post not found', status=404)


@api_view(['DELETE'])
def deletePost(request, postId):
    try:
        post = Post.objects.get(id=postId)
        post.delete()
        return Response(data='Post deleted', status=200)
    except:
        return Response('Post not found', status=404)
