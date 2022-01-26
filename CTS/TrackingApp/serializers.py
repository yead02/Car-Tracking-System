from dataclasses import field
from rest_framework import serializers
from .models import Tracking


class TrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracking
        fields = ['TrackingId','CarID','CurrentLocation']