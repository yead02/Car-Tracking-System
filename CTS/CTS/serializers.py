from rest_framework import serializers

class CTS(serializers.Serializer):
    name = serializers.CharField(max_length = 100)