from rest_framework import filters, viewsets
from rest_framework.pagination import PageNumberPagination

from .models import (BacteriologistUser, BrigadeUser, CompanyUser, DoctorUser,
                     Gender, Group, IdentificationType, PatientUser,
                     ReceptionistUser, UserBase, otherUser)
from .serializers import (BacteriologistSerializer, BrigadeSerializer,
                          CompanySerializer, DoctorSerializer,
                          GenderSerializer, GroupSerializer,
                          IdentificationTypeSerializer, OtherUserSerializer,
                          PatientSerializer, ReceptionistSerializer,
                          UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserBase.objects.all()
    permission_classes = []
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['username']
    ordering_fields = ['username']
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class DoctorViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = DoctorSerializer
    queryset = DoctorUser.objects.all()


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
    queryset = otherUser.objects.all()

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
