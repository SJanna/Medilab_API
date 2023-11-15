from django.shortcuts import render
from rest_framework import viewsets
from .models import Company, MissionCompany
from .serializers import CompanySerializer, MissionCompanySerializer, CompanyListSerializer
# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    
class MissionCompanyViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = MissionCompanySerializer
    queryset = MissionCompany.objects.all()

class CompanyListViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = CompanyListSerializer
    queryset = Company.objects.filter(active=True)