import re

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.db import transaction
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from app.models import UserDevice
from app.serializers.device_serializer import DeviceSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True)
    device_id = serializers.CharField(write_only=True)
    email = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name','password', 'username', 'email','device_id']

    def validate_username(self, value):
        if not re.match(r'^(?=.*[a-zA-Z])(?=.*\d)', value):
            raise serializers.ValidationError("Username must contain both letters and numbers.")
        return value

    def create(self, validated_data):
        device_id = validated_data.pop('device_id')
        validated_data['password'] = make_password(validated_data['password'])
        with transaction.atomic():
            user = User.objects.create(**validated_data)
            UserDevice.objects.create(user=user, device_id=device_id)
        return user
