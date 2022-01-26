#using Model View Set
from .models import City
from .serializers import CitySerializer
from rest_framework import viewsets

class CityMVS(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


