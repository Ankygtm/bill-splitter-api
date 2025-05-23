from django.urls import path
from rest_framework.routers import DefaultRouter

from app.api.auth import Register, Login, GetUser
from app import views

router = DefaultRouter()


urlpatterns = [
    path('', views.home, name='home'),
    path('auth/register', Register.as_view(), name='register'),
    path('auth/login', Login.as_view(), name='login'),
    path('auth/user', GetUser.as_view(), name='user'),
]
urlpatterns += router.urls
