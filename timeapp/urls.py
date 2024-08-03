from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()
router.register(r'time', TimeViewSet)

urlpatterns = [
    path('', include(router.urls))
]