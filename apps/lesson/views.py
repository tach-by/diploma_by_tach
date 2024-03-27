from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from apps.lesson.models import Lesson
from apps.user.models import Pupil
from apps.lesson.serializers import LessonSerializer
from apps.lesson.success_messages import (
    NEW_LESSON_CREATED_MESSAGE,
    LESSON_UPDATED_SUCCESSFULLY_MESSAGE,
    LESSON_WAS_DELETED_SUCCESSFUL
)


class LessonListGenericView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = LessonSerializer

    def get_queryset(self):
        queryset = Lesson.objects.select_related(
            'category',
            'pupil',
            'teacher'
        )

        category = self.request.query_params.get("category")
        teacher = self.request.query_params.get("teacher")
        pupil = self.request.query_params.get("pupil")
        date_from = self.request.query_params.get("date_from")
        date_to = self.request.query_params.get("date_to")

        if category:
            queryset = queryset.filter(
                category__name=category
            )
        if date_from and date_to:
            queryset = queryset.filter(
                created_at__range=[date_from, date_to]
            )
        if pupil:
            queryset = queryset.filter(
                pupil_id=pupil
            )
        if teacher:
            queryset = queryset.filter(
                teaher_id=teacher
            )

        return queryset

    def get(self, request: Request, *args, **kwargs):
        filtered_data = self.get_queryset()

        if filtered_data.exists():
            serializer = self.serializer_class(
                instance=filtered_data,
                many=True
            )

            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data=[]
        )

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def post(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            status=status.HTTP_201_CREATED,
            data={
                "message": NEW_LESSON_CREATED_MESSAGE,
                "data": serializer.data
            }
        )


class LessonDetailGenericView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    def get_object(self):
        lesson_id = self.kwargs.get("lesson_id")

        lesson = get_object_or_404(Lesson, id=lesson_id)

        return lesson

    def get(self, request: Request, *args, **kwargs):
        lesson = self.get_object()

        serializer = self.serializer_class(lesson)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    def put(self, request: Request, *args, **kwargs):
        lesson = self.get_object()

        serializer = self.serializer_class(lesson, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                status=status.HTTP_200_OK,
                data={
                    "message": LESSON_UPDATED_SUCCESSFULLY_MESSAGE,
                    "data": serializer.data
                }
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )

    def delete(self, request, *args, **kwargs):
        lesson = self.get_object()

        lesson.delete()

        return Response(
            status=status.HTTP_200_OK,
            data=LESSON_WAS_DELETED_SUCCESSFUL
        )


class LessonListForParentGenericView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LessonSerializer

    def get_queryset(self):

        user = self.request.user

        pupils = Pupil.objects.filter(user=user)

        queryset = Lesson.objects.filter(pupil__in=pupils)

        return queryset

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def post(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            status=status.HTTP_201_CREATED,
            data={
                "message": NEW_LESSON_CREATED_MESSAGE,
                "data": serializer.data
            }
        )