from dataclasses import field
from rest_framework import serializers
from .models import Operator


class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = ['OperatorId','OperatorName','OperatorCode']