from rest_framework import serializers
from .models import Appointment, Patient, User
from audit_logs.serializers import LogEntrySerializer


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

# Serialiador para la tabla de citas, con el fin de mostrar algunos datos de la cita.
# En la tabla se debe mostrar: Turno, Fecha, Id Paciente, Nombre Paciente, Tipo Examen, Empresa, (Estados) (Botones: Editar, Historia, Ceriticados, otros)
# Solo se muestran los datos, pero no se pueden editar. ni eliminar ni crear.

class AppointmentListSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.user.get_full_name', read_only=True)  
    patient_identification = serializers.CharField(source='patient.user.get_identification', read_only=True)
    company_name = serializers.CharField(source='company.name', read_only=True)
    created_at = serializers.DateTimeField(format="%d/%m/%Y %I:%M %p", read_only=True)
    updated_at = serializers.DateTimeField(format="%d/%m/%Y %I:%M %p", read_only=True)
    registered_by = serializers.CharField(source='registered_by.get_full_name', read_only=True)
    attended_by = serializers.CharField(source='doctor.user.get_full_name', read_only=True)
    exams = serializers.JSONField(source='get_exams', read_only=True)
    package = serializers.CharField(source='package.name', read_only=True)
    is_edited = serializers.BooleanField(read_only=True)

    class Meta:
        model = Appointment
        fields = ['id', 'turn', 'status', 'created_at', 'updated_at', 'patient_identification', 'patient_name', 'evaluation_type','company_name', 'registered_by', 'attended_by', 'exams', 'package', 'is_edited']
        read_only_fields = ['id', 'turn', 'status', 'created_at', 'updated_at', 'patient_identification', 'patient_name', 'evaluation_type','company_name', 'registered_by', 'attended_by', 'exams', 'package', 'is_edited']

