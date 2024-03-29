from rest_framework import serializers
from .models import Tariff, Exam, Package, ExamPrice

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
        model = ExamPrice
        fields = '__all__'
        
class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'
