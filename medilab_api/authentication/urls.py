from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (BrigadeViewSet, CompanyViewSet, DoctorViewSet,
                    GenderViewSet, RoleViewSet, IdentificationTypeViewSet,
                    OtherUserViewSet, PatientViewSet, ReceptionistViewSet,
                    UserViewSet)

router = DefaultRouter()
router.register(r'Roles', RoleViewSet)
router.register(r'IdentificationType', IdentificationTypeViewSet)
router.register(r'Gender', GenderViewSet)
router.register(r'Users', UserViewSet)
router.register(r'Doctors', DoctorViewSet)
router.register(r'Companies', CompanyViewSet)
router.register(r'Patients', PatientViewSet)
router.register(r'Brigades', BrigadeViewSet)
router.register(r'Receptionists', ReceptionistViewSet)
router.register(r'OtherUsers', OtherUserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
]
