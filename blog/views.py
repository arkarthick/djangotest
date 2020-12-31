from django.shortcuts import render
from .models import Post
from rest_framework.response import Response
from .serializer import *
from rest_framework.decorators import api_view
# Create your views here.


# def post_list(request):
#     posts = Post.objects.filter(
#         published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'blog/post_list.html', {'posts': posts})

@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all().order_by('-published_date')  # return list of posts
    serializer = RectSerializer(posts, many=True)
    response = Response(serializer.data)
    # response["Access-Control-Allow-Origin"] = "*"
    # response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    # response["Access-Control-Max-Age"] = "1000"
    # response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return response


@api_view(['GET'])
def view_post(request, pk):
    posts = Post.objects.get(id=pk)  # return list of posts
    serializer = RectSerializer(posts, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def create_post(request):
    serializer = RectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def update_post(request, pk):
    post = Post.objects.get(id=pk)
    serializer = RectSerializer(instance=post, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()

    return Response('post deleted')
