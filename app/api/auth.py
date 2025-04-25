from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

from app.models import UserDevice
from app.serializers.user_serializer import UserSerializer

User = get_user_model()


class Auth(ModelViewSet):
    queryset = User.objects.select_related('user_devices').all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['post'])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

    def get_user_by_device(self, request, device_id=None):
        try:
            device = UserDevice.objects.select_related('user').prefetch_related('user__user_devices').get(
                device_id=device_id)
            user = device.user
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserDevice.DoesNotExist:
            return Response({"detail": "Device not found."}, status=status.HTTP_404_NOT_FOUND)
