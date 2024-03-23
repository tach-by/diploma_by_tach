from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.lesson.error_messages import (
    CATEGORY_NAME_LEN_ERROR_MESSAGE,
    NON_UNIQUE_CATEGORY_NAME_ERROR_MESSAGE,
    CATEGORY_DISCRIPTION_LEN_ERROR_MESSAGE,
    LESSON_DISCRIPTION_LEN_ERROR_MESSAGE
)
from apps.lesson.models import Category, Individuallesson, Grouplesson
from apps.user.models import Pupil, User
from apps.user.serializers import PupilPreviewSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate_name(self, value):
        if Category.objects.filter(name=value).exists():
            raise ValidationError(
                NON_UNIQUE_CATEGORY_NAME_ERROR_MESSAGE
            )

        if len(value) < 4 or len(value) > 25:
            raise ValidationError(
                CATEGORY_NAME_LEN_ERROR_MESSAGE
            )

        return value

    def validate_description(self, value):
        if len(value) > 1500:
            raise ValidationError(
                CATEGORY_DISCRIPTION_LEN_ERROR_MESSAGE
            )

        return value


class IndividuallessonSerializer(serializers.ModelSerializer):
    teacher = serializers.SlugRelatedField(
        slug_field='get_full_name',
        queryset=User.objects.filter(is_staff=True)
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