from .models import *
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from django.http import JsonResponse
from .serializers import PersonSerializers
from rest_framework.decorators import api_view


def home_page(request: Request):
    response = {'message': 'Salom'}
    return JsonResponse(response)


@api_view(http_method_names=["GET"])
def post_list_api_view(request: Request):
    post = Person.objects.all()
    serializer = PersonSerializers(post, many=True)
    response = {
        "message": "GET all posts successfully",
        "data": serializer.data}
    return Response(data=response, status=status.HTTP_200_OK)


@api_view(http_method_names=["POST"])
def post_api_view(request: Request):
    if request.method == "POST":
        data = request.data
        serializer = PersonSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {"data": serializer.data}
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["PUT"])
def put_api_view(request: Request, pk):
    post = get_object_or_404(Person, pk=pk)
    data = request.data
    serializer = PersonSerializers(instance=post, data=data)
    if serializer.is_valid():
        serializer.save()
        response = {"message": "Post update successfully",
                    "data": serializer.data}
        return Response(data=response, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["DELETE"])
def delete_api_view(request: Request, pk):
    post = get_object_or_404(Person, pk=pk)
    post.delete()
    response = {"message": "post delete"}
    return Response(data=response, status=status.HTTP_204_NO_CONTENT)
