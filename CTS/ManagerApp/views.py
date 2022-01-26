#using Model View Set
from .models import Manager
from .serializers import ManagerSerializer
from rest_framework import viewsets

class ManagerMVS(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
