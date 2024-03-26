from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    AllowAny
)
from apps.booking.models import Booking
from apps.user.models import Pupil
from apps.lesson.models import Lesson
from apps.booking.utils import get_week_range
from apps.booking.serializers import (
    BookingSerializer,
    BookingwritableSerializer
)
from apps.booking.success_messages import (
    NEW_BOOKING_CREATED_MESSAGE,
    BOOKING_UPDATED_SUCCESSFULLY_MESSAGE,
    BOOKING_WAS_DELETED_SUCCESSFUL
)


class BookingListGenericView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = BookingSerializer

    def get_queryset(self):
        queryset = Booking.objects.select_related(
            'cabinet',
            'lesson'
        )

        cabinet = self.request.query_params.get("cabinet")
        period = self.request.query_params.get("period")
        date_from = self.request.query_params.get("date_from")
        date_to = self.request.query_params.get("date_to")

        if cabinet:
            queryset = queryset.filter(
                category__name=cabinet
            )
        if date_from and date_to:
            queryset = queryset.filter(
                date__range=[date_from, date_to]
            )

        if period:
            start_of_week, end_of_week = get_week_range(period)
            queryset = queryset.filter(
                date__range=[start_of_week, end_of_week]
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
                "message": NEW_BOOKING_CREATED_MESSAGE,
                "data": serializer.data
            }
        )


class BookingDetailGenericView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = BookingSerializer

    def get_object(self):
        booking_id = self.kwargs.get("booking_id")

        booking = get_object_or_404(Booking, id=booking_id)

        return booking

    def get(self, request: Request, *args, **kwargs):
        booking = self.get_object()

        serializer = self.serializer_class(booking)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    def put(self, request: Request, *args, **kwargs):
        booking = self.get_object()

        serializer = self.serializer_class(booking, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                status=status.HTTP_200_OK,
                data={
                    "message": BOOKING_UPDATED_SUCCESSFULLY_MESSAGE,
                    "data": serializer.data
                }
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )

    def delete(self, request, *args, **kwargs):
        booking = self.get_object()

        booking.delete()

        return Response(
            status=status.HTTP_200_OK,
            data=BOOKING_WAS_DELETED_SUCCESSFUL
        )


class BookingListForParentGenericView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookingSerializer

    def get_queryset(self):
        user = self.request.user

        pupils = Pupil.objects.filter(user=user)

        lessons = Lesson.objects.filter(pupil__in=pupils)

        queryset = Booking.objects.filter(lesson__in=lessons)

        return queryset


class BookingwriteGenericView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookingwritableSerializer

    def get_object(self):
        booking_id = self.kwargs.get("booking_id")

        booking = get_object_or_404(Booking, id=booking_id)

        return booking

    def get(self, request: Request, *args, **kwargs):
        booking = self.get_object()

        serializer = self.serializer_class(booking)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    def put(self, request: Request, *args, **kwargs):
        booking = self.get_object()

        serializer = self.serializer_class(booking, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                status=status.HTTP_200_OK,
                data={
                    "message": BOOKING_UPDATED_SUCCESSFULLY_MESSAGE,
                    "data": serializer.data
                }
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )

class BookingListwritableGenericView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = BookingwritableSerializer

    def get_queryset(self):

        queryset = Booking.objects.filter(writable=True)

        return queryset
