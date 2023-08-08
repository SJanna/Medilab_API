from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    turn = serializers.ReadOnlyField()
    
    class Meta:
        model = Appointment
        
        fields = '__all__'