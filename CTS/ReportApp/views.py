#using Model View Set
from .models import Report
from .serializers import ReportSerializer
from rest_framework import viewsets

class ReportMVS(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


