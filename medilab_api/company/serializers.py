
from rest_framework import serializers
from .models import Company, MissionCompany


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class MissionCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionCompany
        fields = '__all__'
