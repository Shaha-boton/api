# basic_api/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('basic/', views.API_objects.as_view()),
    path('basic/<int:pk>/', views.API_objects_details.as_view()),

    path('product/', views.Product_API_objects.as_view()),
    path('basic/<int:pk>/', views.Product_API_objects_details.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)