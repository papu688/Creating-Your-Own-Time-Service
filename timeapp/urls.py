from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TimeViewSet


router = DefaultRouter()
router.register(r'time', TimeViewSet)

urlpatterns = router.urls