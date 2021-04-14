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
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        comment = models.Comment(body=data['body'], author=request.user, post=data['post'])
        comment.save()
        return Response(status=status.HTTP_201_CREATED)


class CommentListAPIView(ListAPIView):
    serializer_class = serializers.CommentSerializer
    queryset = models.Comment.objects.all()


class CommentDetailAPIView(RetrieveDestroyAPIView):
    serializer_class = serializers.CommentSerializer
    queryset = models.Comment.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]