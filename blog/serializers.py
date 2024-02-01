from rest_framework import serializers
from .models import Main


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = '__all__'
        read_only = ['created_at', 'updated_at']
