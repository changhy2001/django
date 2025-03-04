from django.urls import path
from .api_views import SearchAPIView, SearchDetailAPIView

app_name = "search"

urlpatterns = [
    path('api/', SearchAPIView.as_view(), name='search_api'),
    path('api/<str:username>/', SearchDetailAPIView.as_view(), name='search_detail_api'),
]