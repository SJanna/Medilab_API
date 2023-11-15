
from rest_framework import serializers
from exam.serializers import TariffSerializer
from .models import Company, MissionCompany, Tariff


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


class CompanyListSerializer(serializers.ModelSerializer):
    mission_companies = serializers.SerializerMethodField()
    tariffs = serializers.SerializerMethodField()
# 
    class Meta:
        model = Company
        fields = ['id', 'name', 'mission_companies', 'tariffs']

    def get_tariffs(self, obj):
        active_tariffs = obj.tariff.filter(active=True)
        return TariffSerializer(active_tariffs, many=True).data
    
    def get_mission_companies(self, obj):
        active_mission_companies = obj.company.filter(active=True)
        return MissionCompanySerializer(active_mission_companies, many=True).data
    
