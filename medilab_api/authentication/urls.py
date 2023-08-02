from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RoleViewSet, DoctorViewSet, PatientViewSet, LoginView


router = DefaultRouter()
router.register(r'Users', UserViewSet)
router.register(r'Roles', RoleViewSet)
router.register(r'Doctors', DoctorViewSet)
router.register(r'Patients', PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/login/', LoginView.as_view(), name='login'), # overwrite login
    path('dj-rest-auth/', include('dj_rest_auth.urls')), # include other dj_rest_auth urls
]




# from django.urls import include, path
# from rest_framework.routers import DefaultRouter

# from .views import (BacteriologistViewSet, BrigadeViewSet, CompanyViewSet,
#                     DoctorViewSet, GenderViewSet, IdentificationTypeViewSet,
#                     LoginView, OtherUserViewSet, PatientViewSet,
#                     ReceptionistViewSet, RoleViewSet, UserViewSet,
#                     get_csrf_token, RevalidateUserView)

# router = DefaultRouter()
# router.register(r'Roles', RoleViewSet)
# router.register(r'IdentificationType', IdentificationTypeViewSet)
# router.register(r'Gender', GenderViewSet)
# router.register(r'Users', UserViewSet)
# router.register(r'Doctors', DoctorViewSet)
# router.register(r'Companies', CompanyViewSet)
# router.register(r'Patients', PatientViewSet)
# router.register(r'Brigades', BrigadeViewSet)
# router.register(r'Receptionists', ReceptionistViewSet)
# router.register(r'Bacteriologists', BacteriologistViewSet)
# router.register(r'OtherUsers', OtherUserViewSet)


# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls')),
#     path('dj-rest-auth/login/', LoginView.as_view(), name='login'), # overwrite login
#     path('dj-rest-auth/', include('dj_rest_auth.urls')), # include other dj_rest_auth urls
#     path('get-csrf-token/', get_csrf_token, name='get-csrf-token'), # get csrf token
#     path('revalidate-user/', RevalidateUserView.as_view(), name='revalidate-user'), # revalidate user
# ]
