from rest_framework import serializers
from .models import Company, Doctor, IdentificationType, UserBase, Group

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBase
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
        # read_only_fields = ('sign_in_count', 'last_login', 'last_sign_in_ip')

    def create(self, validated_data):
        user = UserBase.objects.create_user(**validated_data)
        return user
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance

class GruopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}, 'userbase_ptr': {'read_only': True}}
        # read_only_fields = ('sign_in_count', 'last_login', 'last_sign_in_ip')

    def create(self, validated_data):
        user = Doctor.objects.create_user(**validated_data)
        return user
    
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
        # read_only_fields = ('sign_in_count', 'last_login', 'last_sign_in_ip')

    def create(self, validated_data):
        user = Company.objects.create_user(**validated_data)
        return user
    
class IdentificationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentificationType
        fields = '__all__'
