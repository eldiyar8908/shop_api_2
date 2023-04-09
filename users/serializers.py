from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from .models import Confirm


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_password(self, password):
        """custom validation method"""
        return password


class UserLoginValidateSerializer(UserLoginSerializer):
    pass


class UserCreateValidateSerializer(UserLoginSerializer):

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('User already exists')

class UserConfirmValidateSerializer(UserLoginSerializer):

    class Meta:
        model = Confirm
        fields = 'id code'.split()
