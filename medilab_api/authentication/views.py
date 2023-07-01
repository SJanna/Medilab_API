from dj_rest_auth.views import LoginView as DefaultLoginView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import filters, generics, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (BacteriologistUser, BrigadeUser, CompanyUser, DoctorUser,
                     Gender, IdentificationType, OtherUser, PatientUser,
                     ReceptionistUser, Role, UserBase, Profile)
from .permissions import IsOwnerOrAdmin
from .serializers import (BacteriologistSerializer, BrigadeSerializer,
                          CompanySerializer, DoctorSerializer,
                          DoctorUpdateSerializer, GenderSerializer,
                          IdentificationTypeSerializer, OtherUserSerializer,
                          PatientSerializer, ReceptionistSerializer,
                          RoleSerializer, UserSerializer)


# Vistas de autenticación -------------------------------------------------
class LoginView(DefaultLoginView):
    @method_decorator(ensure_csrf_cookie)
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:  # if login was successful
            token = response.data.get('key')  # TOKEN
            if token:
                response.set_cookie('auth_token', token, httponly=True, samesite='Strict', secure=True)
        return response
# -------------------------------------------------------------------------

# Vistas de creación y listado de usuarios --------------------------------
class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            # Si es administrador, mostrar la lista completa de usuarios
            queryset = UserBase.objects.all()
        else:
            # Si no es administrador, filtrar para mostrar solo el usuario autenticado
            queryset = UserBase.objects.filter(id=user.id)
        return queryset
# -------------------------------------------------------------------------

# Vistas de usuarios por rol ---------------------------------------------
class DoctorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = DoctorUser.objects.all()

    def get_serializer_class(self):
        if self.action == 'update':
            return DoctorUpdateSerializer
        return DoctorSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = CompanySerializer
    queryset = CompanyUser.objects.all()

class PatientViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = PatientSerializer
    queryset = PatientUser.objects.all()

class BrigadeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = BrigadeSerializer
    queryset = BrigadeUser.objects.all()

class ReceptionistViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = ReceptionistSerializer
    queryset = ReceptionistUser.objects.all()

class BacteriologistViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = BacteriologistSerializer
    queryset = BacteriologistUser.objects.all()

class OtherUserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = OtherUserSerializer
    queryset = OtherUser.objects.all()


# -------------------------------------------------------------------------

# Vistas de roles, tipos de identificación y géneros ----------------------
class RoleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser] # Un adminUser es aquel que tiene el campo is_staff en True
    serializer_class = RoleSerializer
    queryset = Role.objects.all()

class IdentificationTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = IdentificationTypeSerializer
    queryset = IdentificationType.objects.all()

class GenderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = GenderSerializer
    queryset = Gender.objects.all()
# -------------------------------------------------------------------------