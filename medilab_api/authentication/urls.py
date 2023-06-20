from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (AuditlogViewSet, BacteriologistViewSet, BrigadeViewSet,
                    CompanyViewSet, DoctorViewSet, GenderViewSet,
                    IdentificationTypeViewSet, LoginView, OtherUserViewSet,
                    PatientViewSet, ReceptionistViewSet, RoleViewSet,
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
router.register(r'Bacteriologists', BacteriologistViewSet)
router.register(r'OtherUsers', OtherUserViewSet)
router.register(r'Auditlog', AuditlogViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/login/', LoginView.as_view(), name='login'), # overwrite login
    path('dj-rest-auth/', include('dj_rest_auth.urls')), # include other dj_rest_auth urls
]
