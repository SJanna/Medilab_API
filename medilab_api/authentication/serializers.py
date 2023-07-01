from rest_framework import serializers

from .models import (BacteriologistUser, BrigadeUser, CompanyUser, DoctorUser,
                     Gender, IdentificationType, OtherUser, PatientUser,
                     ReceptionistUser, Role, UserBase, Profile)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


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
        instance.is_active = validated_data.get(
            'is_active', instance.is_active)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.is_superuser = validated_data.get(
            'is_superuser', instance.is_superuser)
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['role','last_login_ip','last_login_date','userbase_ptr', 'login_count']

    def create(self, validated_data):
        validated_data['role'] = Role.objects.get(name=self.Meta.model.__name__.replace('User', ''))
        user = self.Meta.model.objects.create_user(**validated_data)
        return user


class BaseUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        fields = '__all__'
        read_only_fields = ['username', 'role', 'last_login_ip', 'last_login_date', 'userbase_ptr', 'login_count', 'password', 'identification_number', 'role']


# Doctor serializers ----------------------------------------------------------
class DoctorSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = DoctorUser

class DoctorUpdateSerializer(BaseUpdateSerializer):
    class Meta(BaseUpdateSerializer.Meta):
        model = DoctorUser
# ------------------------------------------------------------------------------

# Patient serializers ---------------------------------------------------------
class PatientSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = PatientUser

class PatientUpdateSerializer(BaseUpdateSerializer):
    class Meta(BaseUpdateSerializer.Meta):
        model = PatientUser
# ------------------------------------------------------------------------------

# Company serializers ---------------------------------------------------------
class CompanySerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = CompanyUser

class CompanyUpdateSerializer(BaseUpdateSerializer):
    class Meta(BaseUpdateSerializer.Meta):
        model = CompanyUser
# ------------------------------------------------------------------------------

# Bacteriologist serializers --------------------------------------------------
class BacteriologistSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = BacteriologistUser

class BacteriologistUpdateSerializer(BaseUpdateSerializer):
    class Meta(BaseUpdateSerializer.Meta):
        model = BacteriologistUser
# ------------------------------------------------------------------------------

# Receptionist serializers ----------------------------------------------------
class ReceptionistSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = ReceptionistUser

class ReceptionistUpdateSerializer(BaseUpdateSerializer):
    class Meta(BaseUpdateSerializer.Meta):
        model = ReceptionistUser
# ------------------------------------------------------------------------------

# OtherUser serializers -------------------------------------------------------
class OtherUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = OtherUser

class OtherUserUpdateSerializer(BaseUpdateSerializer):
    class Meta(BaseUpdateSerializer.Meta):
        model = OtherUser
# ------------------------------------------------------------------------------

# Brigade serializers ---------------------------------------------------------
class BrigadeSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = BrigadeUser
    
class BrigadeUpdateSerializer(BaseUpdateSerializer):
    class Meta(BaseUpdateSerializer.Meta):
        model = BrigadeUser
# ------------------------------------------------------------------------------

# Other serializers -----------------------------------------------------------
class IdentificationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentificationType
        fields = '__all__'


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
# ------------------------------------------------------------------------------