from django.urls import path
from . import views


urlpatterns = [
    path('index-api/', views.IndexAPI.as_view(), name='index')  
]