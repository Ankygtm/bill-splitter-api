from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model


# Create your models here.

class UserDevice(Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user_devices')
    device_id = models.CharField(max_length=100)

    class Meta:
        db_table = 'user_devices'
