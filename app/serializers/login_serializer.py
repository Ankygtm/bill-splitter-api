from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        fields = ('username', 'password')

    def validate(self, data):
        try:
            user = User.objects.get(Q(username=data['username']) | Q(email=data['username']))
        except User.DoesNotExist:
            raise serializers.ValidationError({'username': 'Provided credential does not match'})
        if not check_password(data['password'], user.password):
            raise serializers.ValidationError({'username': 'Provided credential does not match'})
        return user
