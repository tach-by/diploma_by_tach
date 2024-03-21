from django.urls import path

from apps.lesson.views import (
    CategoryListGenericView,
    CategoryCreateView,
    RetrieveCategoryGenericView
)


urlpatterns = [
    path("categories", CategoryListGenericView.as_view()),
    path('categories/create/', CategoryCreateView.as_view()),
    path("categories/<int:category_id>/", RetrieveCategoryGenericView.as_view())
]
