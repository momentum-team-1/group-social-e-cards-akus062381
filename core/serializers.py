from django.shortcuts import render
from users.models import User
from .models import Card
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'password', 'cards', 'friend', 'is_staff']
    



class CardSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Card
        fields = [
            'url', 'user', 'message', 'background_color', 'border', 'font',
        ]