from rest_framework import routers
from .views import TariffViewSet, ExamViewSet, ExamPriceViewSet, PackageViewSet

router = routers.DefaultRouter()
router.register(r'Tariff', TariffViewSet)
router.register(r'Exam', ExamViewSet)
router.register(r'ExamPrice', ExamPriceViewSet)
router.register(r'Package', PackageViewSet)

urlpatterns = router.urls                               