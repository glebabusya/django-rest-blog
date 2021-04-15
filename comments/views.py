from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveDestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from news.permissions import IsAuthorOrReadOnly
from . import models, serializers


class CommentCreateAPIView(CreateAPIView):
    serializer_class = serializers.CommentCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        data = serializer.initial_data

        if data['to'][:4] == 'post':
            comment = models.Comment(body=data['body'], author=request.user, post=data['to'][4:])
        else:
            parent_comment = models.Comment.objects.get(pk=int(data['to'][7:]))
            post = models.Post.objects.get(comments=parent_comment)
            comment = models.Comment(body=data['body'], author=request.user, post=post, parentComment=parent_comment)
        comment.save()
        return Response(status=status.HTTP_201_CREATED)


class CommentListAPIView(ListAPIView):
    serializer_class = serializers.CommentSerializer
    queryset = models.Comment.objects.all()


class CommentDetailAPIView(RetrieveDestroyAPIView):
    serializer_class = serializers.CommentSerializer
    queryset = models.Comment.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]