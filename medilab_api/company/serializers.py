
from rest_framework import serializers
from exam.serializers import TariffSerializer
from .models import Company, MissionCompany


class MissionCompanySerializer(serializers.ModelSerializer):
    tariffs = TariffSerializer(many=True, read_only=True, source='tariff')  # Use the related_name 'tariff'
    class Meta:
        model = MissionCompany
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    mission_companies = MissionCompanySerializer(many=True, read_only=True, source='company')  # Use the related_name 'company'
    tariffs = TariffSerializer(many=True, read_only=True, source='tariff')  # Use the related_name 'tariff'
    
    class Meta:
        model = Company
        fields = '__all__'


