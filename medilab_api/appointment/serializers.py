from rest_framework import serializers
from .models import Appointment, Patient, User

class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(default='Patient') 
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['is_superuser', 'is_staff', 'is_active', 'date_joined', 'last_login', 'role']

class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Patient
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = Appointment
        fields = '__all__'
        read_only_fields = ['turn', 'created_at', 'updated_at', 'registered_by']

    def create(self, validated_data):
        patient_data = validated_data.pop('patient')
        user_data = patient_data.pop('user')
        user = User.objects.create(**user_data)
        patient = Patient.objects.create(user=user, **patient_data)
        
        # Obtén el usuario autenticado desde el contexto
        registered_by_user = self.context['request'].user
        
        appointment = Appointment.objects.create(
            patient=patient,
            registered_by=registered_by_user,  # Asigna el usuario autenticado al campo
            **validated_data
        )
        return appointment
