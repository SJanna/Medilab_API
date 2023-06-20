from django.shortcuts import render
from rest_framework import viewsets
from .models import Tariff, Exam, Package, ExamPrice, City
from .serializers import TariffSerializer, ExamSerializer, PackageSerializer, ExamPackageSerializer, CitySerializer
# Create your views here.


class TariffViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = TariffSerializer
    queryset = Tariff.objects.all()
    
class ExamViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()
    
class ExamPriceViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = ExamPackageSerializer
    queryset = ExamPrice.objects.all()
    
class PackageViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = PackageSerializer
    queryset = Package.objects.all()

class CityViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = CitySerializer
    queryset = City.objects.all()