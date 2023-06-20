from rest_framework import serializers

from .models import (BacteriologistUser, BrigadeUser, CompanyUser, DoctorUser,
                     Gender, IdentificationType, PatientUser, ReceptionistUser,
                     Role, UserBase,OtherUser)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBase
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

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

class AuditLogsModelSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        validated_data['created_ip'] = self.context['request'].META['REMOTE_ADDR']

        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['updated_by'] = self.context['request'].user
        validated_data['updated_ip'] = self.context['request'].META['REMOTE_ADDR']

        return super().update(instance, validated_data)


class BaseUserSerializer(AuditLogsModelSerializer):
    class Meta:
        abstract = True
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['created_by', 'updated_by', 'created_at', 'updated_at', 'role', 'userbase_ptr', 'last_login_ip', 'created_ip', 'updated_ip']

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        validated_data['created_ip'] = self.context['request'].META['REMOTE_ADDR']

        #El rol se asigna de acuerdo al nombre del modelo, por ejemplo: DoctorUser -> Doctor
        validated_data['role'] = Role.objects.get(name=self.Meta.model.__name__.replace('User', ''))
        user = self.Meta.model.objects.create_user(**validated_data)
        return user


class DoctorSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = DoctorUser
        

class PatientSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = PatientUser


class CompanySerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = CompanyUser


class BacteriologistSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = BacteriologistUser


class ReceptionistSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = ReceptionistUser


class OtherUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = OtherUser


class BrigadeSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = BrigadeUser


class IdentificationTypeSerializer(AuditLogsModelSerializer):
    class Meta:
        model = IdentificationType
        fields = '__all__'
        read_only_fields = ['created_by', 'updated_by', 'created_at', 'updated_at','created_ip','updated_ip']


class GenderSerializer(AuditLogsModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'
        read_only_fields = ['created_by', 'updated_by', 'created_at', 'updated_at','created_ip','updated_ip']

class RoleSerializer(AuditLogsModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
        read_only_fields = ['created_by', 'updated_by', 'created_at', 'updated_at','created_ip','updated_ip']