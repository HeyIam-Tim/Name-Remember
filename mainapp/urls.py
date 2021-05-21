from django.urls import path
from . import views


urlpatterns = [
    path('index-api/', views.IndexAPI.as_view(), name='index-api'),
    path('name-rememberer/<int:pk>/', views.NameRememberDetailAPI.as_view(), name='delete-api'),
]