from rest_framework import filters, viewsets
from rest_framework.pagination import PageNumberPagination

from .models import (BacteriologistUser, BrigadeUser, CompanyUser, DoctorUser,
                     Gender, Role, IdentificationType, PatientUser,
                     ReceptionistUser, UserBase, OtherUser)
from .serializers import (BacteriologistSerializer, BrigadeSerializer,
                          CompanySerializer, DoctorSerializer,
                          GenderSerializer, RoleSerializer,
                          IdentificationTypeSerializer, OtherUserSerializer,
                          PatientSerializer, ReceptionistSerializer,
                          UserSerializer)


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
