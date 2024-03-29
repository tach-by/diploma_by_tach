from rest_framework import serializers

from apps.user.error_messages import PASSWORDS_DO_NOT_MATCH_ERROR
from apps.user.models import User, Pupil


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=8, write_only=True)
    password2 = serializers.CharField(max_length=68, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'phone',
            'password',
            'password2'
        ]

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")

        if password != password2:
            raise serializers.ValidationError(
                PASSWORDS_DO_NOT_MATCH_ERROR
            )

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data.get("email"),
            first_name=validated_data.get("first_name"),
            last_name=validated_data.get("last_name"),
            phone=validated_data.get("phone"),
            password=validated_data.get("password")
        )

        return user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'username',
            'phone',
            'date_joined'

        ]


class PupilPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pupil
        fields = ['first_name', 'last_name']


class UserInfoSerializer(serializers.ModelSerializer):
    pupils = PupilPreviewSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'username',
            'phone',
            'date_joined',
            'pupils'
        ]


class PupilInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pupil
        fields = [
            'user',
            'first_name',
            'last_name',
            'date_of_birth',
            'description'
        ]
