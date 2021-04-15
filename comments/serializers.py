from rest_framework import serializers

from news.models import Post
from . import models

POSTS_CHOICES = sorted([('post' + str(post.body), post.title) for post in Post.objects.all()])
COMMENT_CHOICES = sorted([('comment' + str(comment.id), comment.body) for comment in models.Comment.objects.all()])
TO_CHOICES = [
    ('Posts', POSTS_CHOICES),
    ('Comments', COMMENT_CHOICES)
]


class CommentCreateSerializer(serializers.ModelSerializer):
    to = serializers.ChoiceField(choices=TO_CHOICES)

    class Meta:
        model = models.Comment
        fields = [
            'id', 'body', 'to'
        ]


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.StringRelatedField()
    author = serializers.StringRelatedField()

    class Meta:
        model = models.Comment
        fields = [
            'id', 'body', 'author', 'post', 'created_time', 'comments', 'parentComment'
        ]

    def get_fields(self):
        fields = super(CommentSerializer, self).get_fields()
        fields['comments'] = CommentSerializer(many=True)
        return fields
