from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsReceptionistUser, IsDoctorUser, IsBacteriologistUser, IsCompanyUser
from .models import UserBase, Group, DoctorUser, CompanyUser, IdentificationType
from .serializers import CompanySerializer, DoctorSerializer, IdentificationTypeSerializer, UserSerializer
from rest_framework.response import Response
from dj_rest_auth.views import LoginView as DefaultLoginView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from auditlog.models import LogEntry
from rest_framework import filters, generics, viewsets
from rest_framework.pagination import PageNumberPagination

class LoginView(DefaultLoginView):
    @method_decorator(ensure_csrf_cookie)
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:  # if login was successful
            token = response.data.get('key')  # TOKEN
            if token:
                response.set_cookie('auth_token', token, httponly=True, samesite='Strict', secure=True)
        return response
    


from .models import (BacteriologistUser, BrigadeUser, CompanyUser, DoctorUser,
                     Gender, IdentificationType, OtherUser, PatientUser,
                     ReceptionistUser, Role, UserBase)
from .serializers import (BacteriologistSerializer, BrigadeSerializer,
                          CompanySerializer, DoctorSerializer,
                          GenderSerializer, IdentificationTypeSerializer,
                          LogEntrySerializer, OtherUserSerializer,
                          PatientSerializer, ReceptionistSerializer,
                          RoleSerializer, UserSerializer)


class AuditlogViewSet(viewsets.ModelViewSet):
    serializer_class = LogEntrySerializer
    queryset= LogEntry.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserBase.objects.all()
    permission_classes = []
    # filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    # search_fields = ['username']
    # ordering_fields = ['username']
    # pagination_class = PageNumberPagination
    # pagination_class.page_size = 10


class RoleViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    # filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    # ordering_fields = ['created_at', 'updated_at']
    # search_fields = ['name']
    # pagination_class = PageNumberPagination
    # pagination_class.page_size = 2

class DoctorViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = DoctorSerializer
    queryset = DoctorUser.objects.all()
    # filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    # search_fields = ['username', 'first_name', 'last_name', 'identification_number']
    # ordering_fields = ['created_at', 'updated_at']
    # pagination_class = PageNumberPagination
    # page_size = 10
    
class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = CompanySerializer
    queryset = CompanyUser.objects.all()


class PatientViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = PatientSerializer
    queryset = PatientUser.objects.all()

class BrigadeViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = BrigadeSerializer
    queryset = BrigadeUser.objects.all()

class ReceptionistViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = ReceptionistSerializer
    queryset = ReceptionistUser.objects.all()

class OtherUserViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = OtherUserSerializer
    queryset = OtherUser.objects.all()

class BacteriologistViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = BacteriologistSerializer
    queryset = BacteriologistUser.objects.all()


class IdentificationTypeViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = IdentificationTypeSerializer
    queryset = IdentificationType.objects.all()


class GenderViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = GenderSerializer
    queryset = Gender.objects.all()
