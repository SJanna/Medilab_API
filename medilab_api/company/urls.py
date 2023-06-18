from rest_framework import routers
from .views import CompanyInfoViewSet, MissionCompanyViewSet, EconomyActivityViewSet

router = routers.DefaultRouter()
router.register(r'EconomyActivity', EconomyActivityViewSet)
router.register(r'CompanyInfo', CompanyInfoViewSet)
router.register(r'MissionCompany', MissionCompanyViewSet)

urlpatterns = router.urls