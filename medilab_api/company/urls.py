from rest_framework import routers
from .views import CompanyViewSet, MissionCompanyViewSet, CompanyListViewSet

router = routers.DefaultRouter()
router.register(r'Company', CompanyViewSet)
router.register(r'MissionCompany', MissionCompanyViewSet)
router.register(r'company_list', CompanyListViewSet)

urlpatterns = router.urls