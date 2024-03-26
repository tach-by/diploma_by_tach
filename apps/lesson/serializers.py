from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.lesson.error_messages import (

    LESSON_DISCRIPTION_LEN_ERROR_MESSAGE
)
from apps.lesson.models import Lesson
from apps.user.models import Pupil, User


class LessonSerializer(serializers.ModelSerializer):
    creator = serializers.StringRelatedField()
    teacher = serializers.SlugRelatedField(
        slug_field='get_full_name',
        queryset=User.objects.filter(is_staff=True)
    )
    pupil = serializers.SlugRelatedField(
        slug_field='get_full_name',
        queryset=Pupil.objects.all(),
    )
    category = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Pupil.objects.all()
    )

    class Meta:
        model = Lesson
        fields = ['creator', 'teacher', 'category', 'description', 'pupil']

    def validate_description(self, value):
        if len(value) > 1500:
            raise ValidationError(
                LESSON_DISCRIPTION_LEN_ERROR_MESSAGE
            )

        return value


