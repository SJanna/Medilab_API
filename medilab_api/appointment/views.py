from django.shortcuts import render
from rest_framework import viewsets
from .models import DoctorInfo, Appointment, CompanyInfo, MissionCompany, Tariff, Exam, ExamPackage, Package, CompanySection
from .serializers import DoctorInfoSerializer, AppointmentSerializer, CompanyInfoSerializer, MissionCompanySerializer, TariffSerializer, ExamSerializer, ExamPackageSerializer, PackageSerializer, CompanySectionSerializer
# Create your views here.

class DoctorInfoViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = DoctorInfoSerializer
    queryset = DoctorInfo.objects.all()
    
class AppointmentViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

class CompanyInfoViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = CompanyInfoSerializer
    queryset = CompanyInfo.objects.all()

class MissionCompanyViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = MissionCompanySerializer
    queryset = MissionCompany.objects.all()
    
class TariffViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = TariffSerializer
    queryset = Tariff.objects.all()
    
class ExamViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()
    
class ExamPackageViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = ExamPackageSerializer
    queryset = ExamPackage.objects.all()
    
class PackageViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = PackageSerializer
    queryset = Package.objects.all()

class CompanySectionViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = CompanySectionSerializer
    queryset = CompanySection.objects.all()