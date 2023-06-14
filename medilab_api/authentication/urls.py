from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, DoctorViewSet, GroupViewSet, IdentificationTypeViewSet, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'Doctors', DoctorViewSet)
router.register(r'Companies', CompanyViewSet)
router.register(r'IdentificationType', IdentificationTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
]
