from rest_framework.generics import (
    get_object_or_404,
    CreateAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from apps.user.serializers import (
    UserRegisterSerializer,
    UserListSerializer,
    UserInfoSerializer,
    PupilInfoSerializer
)
from apps.user.models import User, Pupil
from apps.user.success_messages import (
    PUPIL_UPDATED_SUCCESSFULLY_MESSAGE,
    NEW_PUPIL_CREATED_MESSAGE,
    PUPIL_WAS_DELETED_SUCCESSFUL
)


class UserRegistrationGenericView(CreateAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                status=status.HTTP_201_CREATED,
                data=serializer.data
            )
        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer.errors
        )


class ListUsersGenericView(ListAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = UserListSerializer

    def get_queryset(self):
        users = User.objects.exclude(
            id=self.request.user.id
        )

        return users

    def get(self, request: Request, *args, **kwargs):
        users = self.get_queryset()

        if not users:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data=[]
            )

        serializer = self.serializer_class(users, many=True)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )


class UserDetailGenericView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserInfoSerializer

    def get_object(self):
        user_id = self.kwargs.get("user_id")

        user_obj = get_object_or_404(User, id=user_id)

        return user_obj

    def get(self, request: Request, *args, **kwargs):
        user = self.get_object()

        serializer = self.serializer_class(user)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    def put(self, request: Request, *args, **kwargs):
        user = self.get_object()

        serializer = self.serializer_class(
            user,
            data=request.data,
            partial=True
        )

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )
        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer.errors
        )

    def delete(self, request: Request, *args, **kwargs):
        user = self.get_object()

        user.delete()

        return Response(
            status=status.HTTP_200_OK,
            data=[]
        )


class PupilDetailGenericView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PupilInfoSerializer

    def get_object(self):
        pupil_id = self.kwargs.get("pupil_id")
        pupil_obj = get_object_or_404(Pupil, id=pupil_id)
        return pupil_obj

    def get(self, request: Request, *args, **kwargs):
        pupil = self.get_object()
        serializer = self.serializer_class(pupil)
        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    def put(self, request: Request, *args, **kwargs):
        pupil = self.get_object()
        serializer = self.serializer_class(
            pupil,
            data=request.data,
            partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                status=status.HTTP_200_OK,
                data={
                    "message": PUPIL_UPDATED_SUCCESSFULLY_MESSAGE,
                    "data": serializer.data
                }
            )
        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer.errors
        )

    def delete(self, request: Request, *args, **kwargs):
        pupil = self.get_object()
        pupil.delete()
        return Response(
            status=status.HTTP_200_OK,
            data=PUPIL_WAS_DELETED_SUCCESSFUL
        )


class ListPupilsOfUserGenericView(ListCreateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = PupilInfoSerializer

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        pupils = Pupil.objects.filter(user_id=user_id)
        return pupils

    def get(self, request: Request, *args, **kwargs):
        pupils = self.get_queryset()

        if not pupils:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data=[]
            )

        serializer = self.serializer_class(pupils, many=True)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    def post(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                status=status.HTTP_201_CREATED,
                data={
                    "message": NEW_PUPIL_CREATED_MESSAGE,
                    "data": serializer.data
                }
            )
        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer.errors
        )