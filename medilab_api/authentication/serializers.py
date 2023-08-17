from rest_framework import serializers
from .models import User, Role, Doctor, Patient
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)
    
    
class RevalidateUserSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'role']
        

class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = '__all__'
        

class DoctorNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name','last_name']
        
        

        


# class UserSerializer(serializers.ModelSerializer):
#     role = serializers.StringRelatedField()

#     class Meta:
#         model = UserBase
#         fields = '__all__'
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = UserBase.objects.create_user(**validated_data)
#         return user

#     def update(self, instance, validated_data):
#         instance.username = validated_data.get('username', instance.username)
#         instance.is_active = validated_data.get(
#             'is_active', instance.is_active)
#         instance.is_staff = validated_data.get('is_staff', instance.is_staff)
#         instance.is_superuser = validated_data.get(
#             'is_superuser', instance.is_superuser)
#         instance.set_password(validated_data.get('password'))
#         instance.save()
#         return instance


# class BaseUserSerializer(serializers.ModelSerializer):

#     class Meta:
#         abstract = True
#         fields = '__all__'
#         extra_kwargs = {'password': {'write_only': True}}
#         read_only_fields = ['role','last_login_ip','userbase_ptr']

#     def create(self, validated_data):
#         validated_data['role'] = Role.objects.get(name=self.Meta.model.__name__.replace('User', ''))
#         validated_data['last_login_ip'] = self.context['request'].META['REMOTE_ADDR']
#         user = self.Meta.model.objects.create_user(**validated_data)
#         return user


# class DoctorSerializer(BaseUserSerializer):
#     class Meta(BaseUserSerializer.Meta):
#         model = DoctorUser


# class PatientSerializer(BaseUserSerializer):
#     class Meta(BaseUserSerializer.Meta):
#         model = PatientUser


# class CompanySerializer(BaseUserSerializer):
#     role = serializers.StringRelatedField()

#     class Meta(BaseUserSerializer.Meta):
#         model = CompanyUser


# class BacteriologistSerializer(BaseUserSerializer):
#     class Meta(BaseUserSerializer.Meta):
#         model = BacteriologistUser


# class ReceptionistSerializer(BaseUserSerializer):
#     class Meta(BaseUserSerializer.Meta):
#         model = ReceptionistUser


# class OtherUserSerializer(BaseUserSerializer):
#     class Meta(BaseUserSerializer.Meta):
#         model = OtherUser


# class BrigadeSerializer(BaseUserSerializer):
#     class Meta(BaseUserSerializer.Meta):
#         model = BrigadeUser


# class IdentificationTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = IdentificationType
#         fields = '__all__'


# class GenderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Gender
#         fields = '__all__'


# class RoleSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Role
#         fields = '__all__'
