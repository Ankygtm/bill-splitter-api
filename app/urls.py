from django.urls import path
from rest_framework.routers import DefaultRouter

from app.api.auth import Auth
from app.api import auth
from app import views

router = DefaultRouter()

router.register(r'auth', Auth, basename='auth')
me = Auth.as_view({
    'get': 'get_user_by_device',
})
urlpatterns = [
    path('', views.home, name='home'),
    path(r'auth/<str:device_id>/', me, name='me'),
]
urlpatterns += router.urls
