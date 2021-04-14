from rest_framework import serializers

from news.models import Post
from . import models


class CommentCreateSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects)

    class Meta:
        model = models.Comment
        fields = [
            'id', 'body', 'post'
        ]


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.StringRelatedField()
    author = serializers.StringRelatedField()

    class Meta:
        model = models.Comment
        fields = [
            'id', 'body', 'author', 'post', 'created_time'
        ]
