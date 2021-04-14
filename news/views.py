from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models, serializers, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PostCreateAPIView(APIView):
    serializer_class = serializers.PostCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        post = models.Post(title=data['title'], body=data['body'], author=request.user)
        post.slug = post.generate_slug()
        post.save()
        return Response(
            status=status.HTTP_201_CREATED
        )


class PostListAPIView(ListAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, permissions.IsAuthorOrReadOnly]
