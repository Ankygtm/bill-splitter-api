from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.jwt import generate_jwt
from app.models import UserDevice
from app.response import ApiResponse
from app.serializers.login_serializer import LoginSerializer
from app.serializers.user_serializer import UserSerializer

User = get_user_model()


class Register(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = generate_jwt(UserSerializer(user).data)
            payload = {"token": token, "user": user}
            return ApiResponse.success(payload, "User Registered Successfully")


class Login(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data
            token = generate_jwt(UserSerializer(user).data)
            payload = {"token": token, "user": UserSerializer(user).data}
            return ApiResponse.success(payload, "User Logged In Successfully")
