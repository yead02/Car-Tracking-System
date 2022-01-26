#using Model View Set
from .models import Operator
from .serializers import OperatorSerializer
from rest_framework import viewsets

class OperatorMVS(viewsets.ModelViewSet):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer



#using Concrete view class
"""
from .models import Operator
from . serializers import OperatorSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# List and Create - PK not required
class OperatorLC(ListCreateAPIView):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer

# Retrieve Update and Destroy - PK required
class OperatorRUD(RetrieveUpdateDestroyAPIView):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer

"""


#using GenericAPIView and Model Mixin
"""

from .models import Operator
from . serializers import OperatorSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin , CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

# List and Create - PK not required
class OperatorLC(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# Retrieve Update and Destroy - PK required
class OperatorRUD(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


"""



#regular view
"""
from django.http import request, response
from django.shortcuts import render #
from rest_framework.decorators import api_view
from rest_framework.response import Response #
from uritemplate import partial
from .models import Operator #
from .serializers import OperatorSerializer #
from rest_framework import status #
from rest_framework.views import APIView #


class OperatorAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            ope = Operator.objects.get(id=id)
            serializer = OperatorSerializer(ope)
            return Response(serializer.data)
        ope = Operator.objects.all()
        serializer = OperatorSerializer(ope, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OperatorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'})
        return Response(serializer.errors)

    def put(self, request, pk=None, format=None):
        id = pk
        ope = Operator.objects.get(pk=id)
        serializer = OperatorSerializer(ope, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)

    def patch(self, request, pk=None, format=None):
        id = pk
        ope = Operator.objects.get(pk=id)
        serializer = OperatorSerializer(ope, data=request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)

    def patch(self, request, pk=None, format=None):
        id = pk
        ope = Operator.objects.get(pk=id)
        ope.delete()
        return Response({'msg':'Data Updated'})


"""
