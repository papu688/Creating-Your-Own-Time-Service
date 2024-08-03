from rest_framework import viewsets
from .models import Time
from .serializers import TimeSerializer

class TimeViewSet(viewsets.ModelViewSet):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer