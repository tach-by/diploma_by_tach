from django.urls import path
from apps.category.views import (
    CategoryListGenericView,
    CategoryCreateView,
    RetrieveCategoryGenericView
)


urlpatterns = [
    path("", CategoryListGenericView.as_view()),
    path('create/', CategoryCreateView.as_view()),
    path("<int:category_id>/", RetrieveCategoryGenericView.as_view())
]