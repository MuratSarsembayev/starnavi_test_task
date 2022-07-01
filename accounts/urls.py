from django.urls import path, include
from .views import RegisterApi

urlpatterns = [
      path('api/v1/register', RegisterApi.as_view()),
]
