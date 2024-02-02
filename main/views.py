from urllib.request import Request

from django.shortcuts import render, get_object_or_404
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from .serializers import AuthorSerializer
from .models import Author


@api_view(["GET"])
def getApiView(request: Request):
    post = Author.objects.all()
    serializer = AuthorSerializer(post, many=True)
    response = {"message": "Get",
                "data": serializer.data}
    return Response(data=response, status=status.HTTP_200_OK)


@api_view(["POST"])
def createApiView(request: Request):
    if request.method == "POST":
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def updateApiView(request: Request, pk):
    author = get_object_or_404(Author, pk=pk)
    data = request.data
    serializer = AuthorSerializer(instance=author, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(data=data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def deleteApiView(request: Request, pk):
    author = get_object_or_404(Author, pk = pk)
    author.delete()
    return Response(data=request.data, status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def detailApiView(request: Request, pk):
    author = get_object_or_404(Author, pk = pk)
    serializer = AuthorSerializer(author)
    return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)

