from rest_framework import serializers
from .models import NetworkNode


class NetworkNodeSerializer(serializers.ModelSerializer):
    level = serializers.ReadOnlyField()

    class Meta:
        model = NetworkNode
        fields = (
            "id",
            "name",
            "email",
            "country",
            "city",
            "street",
            "house_number",
            "supplier",
            "debt",
            "created_at",
            "level",
        )
        read_only_fields = ("created_at", "level")