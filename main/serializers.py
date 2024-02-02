from rest_framework import serializers
from .models import *


# class PostSerializers(serializers.ModelSerializer):
#     title = serializers.CharField(max_length=212)
#     des = serializers.CharField()
#
#     def validate(self, attrs):
#         title = attrs.get('title')
#         des = attrs.get('des')
#         return attrs
#
#     def create(self, validated_data):
#         return Post.objects.create(**validated_data)


class PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'age']

