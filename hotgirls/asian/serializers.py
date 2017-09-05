from rest_framework import serializers
from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'title', 'cover')


class AlbumDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'content')