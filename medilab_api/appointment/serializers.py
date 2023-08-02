from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.Serializer):
    class Meta:
        model = Appointment
        field = '__all__'