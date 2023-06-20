from rest_framework import serializers
from .models import DoctorInfo, Appointment, CompanySection

class DoctorInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorInfo
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
        
class CompanySectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanySection
        fields = '__all__'