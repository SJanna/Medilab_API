from django.shortcuts import render
from rest_framework import viewsets
from .models import DoctorInfo, Appointment, CompanySection
from .serializers import DoctorInfoSerializer, AppointmentSerializer, CompanySectionSerializer
# Create your views here.

class DoctorInfoViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = DoctorInfoSerializer
    queryset = DoctorInfo.objects.all()
    
class AppointmentViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

class CompanySectionViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = CompanySectionSerializer
    queryset = CompanySection.objects.all()