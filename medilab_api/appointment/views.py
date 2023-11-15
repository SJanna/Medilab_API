from rest_framework import viewsets
from .models import Appointment
from auditlog.models import LogEntry
from .serializers import AppointmentSerializer, AppointmentListSerializer, AppointmetFormDataSerializer
from audit_logs.serializers import LogEntrySerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.response import Response
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
    
from django.http import JsonResponse
from .models import Doctor, Company
from exam.models import ExamPrice, Exam
from company.models import MissionCompany
from exam.models import Tariff

class AppointmentFormData(generics.ListAPIView):
    def list(self, request, *args, **kwargs):
        doctors = Doctor.objects.filter(user__is_active=True)
        exams = Exam.objects.filter(active=True)
        companies = Company.objects.filter(active=True)
        # mission_companies = MissionCompany.objects.filter(active=True)
        # tariff = Tariff.objects.filter(active=True)

        data = {
            'doctors': list(doctors.values('id', 'user__first_name', 'user__last_name')),
            'exams': list(exams.values('id', 'name', 'type__name', 'type__icon', 'category')),
            'companies': list(companies.values('id', 'name')),
            # 'mission_companies': list(mission_companies.values('id', 'name', 'company__name', 'active', 'company__id')),
            # 'tariff': list(tariff.values('id', 'name', 'active', 'exams_prices__exam__name', 'exams_prices__price', 'exams_prices__exam__id')),
        }
        return JsonResponse(data)
    
# Lista de logs de la tabla de citas
class LogEntryList(generics.ListAPIView):
    serializer_class = LogEntrySerializer
    queryset = LogEntry.objects.filter(content_type__model='appointment')