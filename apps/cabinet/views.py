from apps.cabinet.serializers import CabinetSerializer
from apps.cabinet.models import Cabinet
from rest_framework.viewsets import ModelViewSet


class CabinetViewSet(ModelViewSet):
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer