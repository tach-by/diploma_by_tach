from apps.cabinet.serializers import CabinetSerializer
from apps.cabinet.models import Cabinet
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
)

class CabinetViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer