from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import BlogUser


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, min_length=8, write_only=True)
    password_confirm = serializers.CharField(max_length=255, min_length=8, write_only=True)

    class Meta:
        model = BlogUser
        fields = [
            'email', 'password', 'password_confirm'
        ]

    def create(self, validated_data):
        if validated_data.get('password') != validated_data.get('password_confirm'):
            raise serializers.ValidationError('Passwords must match')
        validated_data.pop('password_confirm')
        return BlogUser.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = BlogUser
        fields = [
            'email', 'password'
        ]

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in'
            )
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in'
            )

        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found'
            )

        return data



