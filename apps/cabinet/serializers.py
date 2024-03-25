from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from apps.cabinet.models import Cabinet
from apps.cabinet.error_messages import (
    CABINET_DISCRIPTION_LEN_ERROR_MESSAGE
)
class CabinetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabinet
        fields = '__all__'

    def validate_description(self, value):
        if len(value) > 1500:
            raise ValidationError(
                CABINET_DISCRIPTION_LEN_ERROR_MESSAGE
            )

        return value