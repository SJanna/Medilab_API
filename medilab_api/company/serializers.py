
from rest_framework import serializers
from .models import Company, MissionCompany


class MissionCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionCompany
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    mission_companies = MissionCompanySerializer(many=True, read_only=True, source='company')  # Use the related_name 'company'
    
    class Meta:
        model = Company
        fields = '__all__'


