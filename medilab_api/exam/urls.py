from rest_framework import routers
from .views import TariffViewSet, ExamViewSet, ExamPriceViewSet, PackageViewSet, CityViewSet

router = routers.DefaultRouter()
router.register(r'Tariff', TariffViewSet)
router.register(r'Exam', ExamViewSet)
router.register(r'ExamPrice', ExamPriceViewSet)
router.register(r'Package', PackageViewSet)
router.register(r'City', CityViewSet)

urlpatterns = router.urls