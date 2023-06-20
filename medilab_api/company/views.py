from rest_framework import viewsets
from .models import CompanyInfo, MissionCompany, EconomyActivity
from .serializers import CompanyInfoSerializer, MissionCompanySerializer, EconomyActivitySerializer
# Create your views here.

class CompanyInfoViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = CompanyInfoSerializer
    queryset = CompanyInfo.objects.all()

class MissionCompanyViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = MissionCompanySerializer
    queryset = MissionCompany.objects.all()

class EconomyActivityViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = EconomyActivitySerializer
    queryset = EconomyActivity.objects.all()