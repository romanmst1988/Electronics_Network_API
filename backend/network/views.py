from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from .models import NetworkNode
from .serializers import NetworkNodeSerializer
from users.permissions import IsActiveEmployee


class NetworkNodeViewSet(ModelViewSet):
    queryset = NetworkNode.objects.all().select_related("supplier")
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveEmployee]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("country",)