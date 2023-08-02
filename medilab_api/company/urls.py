from rest_framework import routers
from .views import CompanyViewSet, MissionCompanyViewSet

router = routers.DefaultRouter()
router.register(r'Company', CompanyViewSet)
router.register(r'MissionCompany', MissionCompanyViewSet)

urlpatterns = router.urls