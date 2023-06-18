from rest_framework import serializers
from .models import DoctorInfo, CompanyInfo, Appointment, MissionCompany, Tariff, Exam, ExamPackage, Package, CompanySection

class DoctorInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorInfo
        fields = '__all__'
        
class CompanyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = '__all__'
        
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
        
class MissionCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionCompany
        fields = '__all__'
        
class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = '__all__'

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'

class ExamPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamPackage
        fields = '__all__'
        
class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'
        
class CompanySectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanySection
        fields = '__all__'