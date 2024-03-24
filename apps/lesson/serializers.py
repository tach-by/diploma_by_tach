from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.lesson.error_messages import (

    LESSON_DISCRIPTION_LEN_ERROR_MESSAGE
)
from apps.lesson.models import Individuallesson, Grouplesson
from apps.user.models import Pupil, User
from apps.user.serializers import PupilPreviewSerializer


class IndividuallessonSerializer(serializers.ModelSerializer):
    teacher = serializers.SlugRelatedField(
        slug_field='get_full_name',
        queryset=User.objects.filter(is_staff=True)
    )
    pupil = serializers.SlugRelatedField(
        slug_field='get_full_name',
        queryset=Pupil.objects.all()
    )
    class Meta:
        model = Individuallesson
        fields = ['creator', 'teacher','category', 'description', 'created_at', 'updated_at', 'pupil']

    def validate_description(self, value):
        if len(value) > 1500:
            raise ValidationError(
                LESSON_DISCRIPTION_LEN_ERROR_MESSAGE
            )

        return value

class GrouplessonSerializer(serializers.ModelSerializer):
    teacher = serializers.SlugRelatedField(
        slug_field='get_full_name',
        queryset=User.objects.filter(is_staff=True)
    )
    pupils = serializers.SlugRelatedField(
        slug_field='get_full_name',
        queryset=Pupil.objects.all()
    )

    class Meta:
        model = Grouplesson
        fields = ['creator','teacher', 'category', 'description', 'created_at', 'updated_at', 'pupils']