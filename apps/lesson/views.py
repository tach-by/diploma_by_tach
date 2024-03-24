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
from apps.lesson.models import (
    Individuallesson,
    Grouplesson
)
from apps.lesson.serializers import (
    IndividuallessonSerializer,
    GrouplessonSerializer
)

class IndividuallessonListGenericView(ListCreateAPIView):
    serializer_class = IndividuallessonSerializer

    def get_queryset(self):
        queryset = Individuallesson.objects.select_related(
            'category'
        )

        status_obj = self.request.query_params.get("status")
        category = self.request.query_params.get("category")
        date_from = self.request.query_params.get("date_from")
        date_to = self.request.query_params.get("date_to")
        deadline = self.request.query_params.get("deadline")

        if status_obj:
            queryset = queryset.filter(
                status__name=status_obj
            )
        if category:
            queryset = queryset.filter(
                category__name=category
            )
        if date_from and date_to:
            queryset = queryset.filter(
                date_started__range=[date_from, date_to]
            )
        if deadline:
            queryset = queryset.filter(
                deadline=deadline
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

    def post(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            status=status.HTTP_201_CREATED,
            data={
                "message": NEW_SUBTASK_CREATED_MESSAGE,
                "data": serializer.data
            }
        )