from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorInfoViewSet, AppointmentViewSet, CompanySectionViewSet

router = DefaultRouter()
router.register(r'DoctorInfo', DoctorInfoViewSet)
router.register(r'Appointment', AppointmentViewSet)
router.register(r'CompanySection', CompanySectionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]