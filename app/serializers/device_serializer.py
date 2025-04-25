from rest_framework import serializers

from app.models import UserDevice


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDevice
        fields = ['device_id']