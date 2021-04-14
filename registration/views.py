from rest_framework import status
from django.contrib.auth import logout, login
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models, serializers, permissions


class RegistrationAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            status=status.HTTP_201_CREATED
        )


class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.LoginSerializer

    def post(self, request):

        if not isinstance(request.user, models.BlogUser):
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)

            user = serializer.validate(request.data)
            login(request, user)
            return Response(
                status=status.HTTP_200_OK
            )
        else:
            return Response(data={'message': 'user must be logged out'})


class LogoutAPIView(APIView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UsersListAPIView(ListAPIView):
    serializer_class = serializers.UserSerializer
    queryset = models.BlogUser.objects.all()


class UserDetailAPIView(RetrieveUpdateAPIView):
    queryset = models.BlogUser.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, permissions.IsCurrentUserOrReadOnly]
