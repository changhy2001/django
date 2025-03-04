from django.urls import path
from . import views
from .api_views import RegisterAPIView, LoginAPIView, LogoutAPIView, AuthStatusAPIView

app_name = 'users'

urlpatterns = [
    path('api/auth-status/', AuthStatusAPIView.as_view(), name='api_auth_status'),
    path('api/register/', RegisterAPIView.as_view(), name='api_register'),
    path('api/login/', LoginAPIView.as_view(), name='api_login'),
    path('api/logout/', LogoutAPIView.as_view(), name='api_logout'),
]