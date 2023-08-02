from rest_framework import viewsets
from .models import Appointment
from .serializers import AppointmentSerializer

# Create your views here.
class AppointmentViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
