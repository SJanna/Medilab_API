from rest_framework import viewsets
from .models import Appointment
from auditlog.models import LogEntry
from .serializers import AppointmentSerializer, AppointmentListSerializer
from audit_logs.serializers import LogEntrySerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
# Create your views here.
class AppointmentViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    
    # def perform_create(request, serializer):
    #     serializer.save(registered_by=request.user)

# Lista de appointmes con la información ensencial para la tabla de citas
class AppointmentList(generics.ListAPIView):
    serializer_class = AppointmentListSerializer
    queryset = Appointment.objects.all()
    pagination_class = LimitOffsetPagination
    pagination_class.default_limit = 3
    # filtro a través de la url por fecha, reecibiendo los parametros start_date y end_date en formato DD-MM-YYYY,
    # que filtrará según la fecha de creación de la cita.
    def get_queryset(self):
        queryset = Appointment.objects.all()
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        if start_date is not None and end_date is not None:
            queryset = queryset.filter(created_at__date__range=[start_date, end_date])
        return queryset
# ejemplo de url para filtrar por fecha: http://localhost:8000/appointment/AppointmentsList/?start_date=2021-01-01&end_date=2021-01-31

# Lista de logs de la tabla de citas
class LogEntryList(generics.ListAPIView):
    serializer_class = LogEntrySerializer
    queryset = LogEntry.objects.filter(content_type__model='appointment')