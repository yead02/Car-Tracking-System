#using Model View Set
from .models import Car
from .serializers import CarSerializer
from rest_framework import viewsets

class CarMVS(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


