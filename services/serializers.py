from rest_framework import serializers

from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            "id",
            "title",
            "receiver",
            "provider",
            "description",
            "date",
            "status",
            "valoration",
        ]
