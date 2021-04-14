from rest_framework import serializers
from . import models


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = [
            'title', 'body'
        ]


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    comments = serializers.StringRelatedField(many=True)
    slug = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = models.Post
        fields = [
            'id', 'slug', 'author', 'title', 'body', 'created_time', 'updated_time', 'comments'
        ]
