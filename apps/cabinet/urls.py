from rest_framework.routers import DefaultRouter

from apps.cabinet.views import CabinetViewSet


router = DefaultRouter()

router.register('', CabinetViewSet)

urlpatterns = router.urls