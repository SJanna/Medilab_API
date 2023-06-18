from rest_framework import serializers
from .models import CompanyInfo, MissionCompany, EconomyActivity

class CompanyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = '__all__'
        
class MissionCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionCompany
        fields = '__all__'

class EconomyActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = EconomyActivity
        fields = '__all__'