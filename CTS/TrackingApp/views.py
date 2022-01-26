#using Model View Set
from .models import Tracking
from .serializers import TrackingSerializer
from rest_framework import viewsets

class TrackingMVS(viewsets.ModelViewSet):
    queryset = Tracking.objects.all()
    serializer_class = TrackingSerializer


