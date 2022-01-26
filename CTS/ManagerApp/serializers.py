from dataclasses import field
from rest_framework import serializers
from .models import Manager


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['ManagerId','ManagerName','ManagerPassword']