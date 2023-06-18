from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsReceptionistUser, IsDoctorUser, IsBacteriologistUser, IsCompanyUser
from .models import UserBase, Group, DoctorUser, CompanyUser, IdentificationType
from .serializers import CompanySerializer, DoctorSerializer, GruopSerializer, IdentificationTypeSerializer, UserSerializer
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserBase.objects.all()
    permission_classes = []


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = GruopSerializer
    queryset = Group.objects.all()


class DoctorViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = DoctorSerializer
    queryset = DoctorUser.objects.all()

class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = CompanySerializer
    queryset = CompanyUser.objects.all()

class IdentificationTypeViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = IdentificationTypeSerializer
    queryset = IdentificationType.objects.all()