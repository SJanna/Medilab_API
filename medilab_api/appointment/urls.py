from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorInfoViewSet, AppointmentViewSet, CompanyInfoViewSet, MissionCompanyViewSet, TariffViewSet, ExamViewSet, ExamPackageViewSet, PackageViewSet, CompanySectionViewSet

router = DefaultRouter()
router.register(r'DoctorInfo', DoctorInfoViewSet)
router.register(r'Appointment', AppointmentViewSet)
router.register(r'CompanyInfo', CompanyInfoViewSet)
router.register(r'MissionCompany', MissionCompanyViewSet)
router.register(r'Tariff', TariffViewSet)
router.register(r'Exam', ExamViewSet)
router.register(r'ExamPackage', ExamPackageViewSet)
router.register(r'Package', PackageViewSet)
router.register(r'CompanySection', CompanySectionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]