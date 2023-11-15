from django.db import models
from authentication.models import User, Patient, Doctor
from company.models import Company
from exam.models import Package
from exam.models import AppointmentExam
from django.utils import timezone

class Accompanist(models.Model):
    indentification_type = models.CharField(max_length=55)
    identification = models.CharField(max_length=55)
    name = models.CharField(max_length=55)
    phone = models.CharField(max_length=55)
    email = models.CharField(max_length=55)
    relationship = models.CharField(max_length=55)
    
    def __str__(self):
        return self.name
    

class Appointment(models.Model):
    turn = models.IntegerField()
    # Información del paciente -----------------------------------------------------------------------------------
    patient = models.ForeignKey(Patient, models.DO_NOTHING) # Incluye toda la información del paciente
    # ------------------------------------------------------------------------------------------------------------
    # Empresa: (mission company) ---------------------------------------------------------------------------------
    company = models.ForeignKey(Company, models.DO_NOTHING) # Incluye el tarifario de la empresa
    # ------------------------------------------------------------------------------------------------------------
    # Información del Médico -------------------------------------------------------------------------------------
    doctor = models.ForeignKey(Doctor, models.DO_NOTHING)
    # ------------------------------------------------------------------------------------------------------------
    # Datos de la recepción --------------------------------------------------------------------------------------
    city = models.CharField(max_length=255) # City where the patient is registered.
    evaluation_type = models.CharField(max_length=255)
    payment_type = models.CharField(max_length=50, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)  # Observations
    exams = models.ManyToManyField(AppointmentExam, related_name='appointment_exams', blank=True) # Lista de exámenes
    package = models.ForeignKey(Package, models.DO_NOTHING, blank=True, null=True)
    # Acompañante -----------------------------------------------------------------------------------------------
    accompanist = models.ForeignKey(Accompanist, on_delete=models.DO_NOTHING, blank=True, null=True)
    # ------------------------------------------------------------------------------------------------------------
    total_amount = models.FloatField()
    status = models.CharField(max_length=255, default='PENDIENTE') # Pendiente, Atendido, Cancelado, No asistió
    # ------------------------------------------------------------------------------------------------------------
    # Otros datos ------------------------------------------------------------------------------------------------
    registered_by = models.ForeignKey(User, models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # ------------------------------------------------------------------------------------------------------------
    
    def __str__(self):
        return str(self.turn) + str(self.doctor)
    
    def get_exams(self): 
        return [{'exam_name': exam.exam_price.exam.name, 'price': exam.exam_price.price, 'type': exam.exam_price.exam.type.name, 'icon': exam.exam_price.exam.type.icon, 'category':exam.exam_price.exam.category, 'state':exam.status, 'request_date':exam.request_date, 'completion_date':exam.completion_date} for exam in self.exams.all()]  

    def is_edited(self):
        return self.created_at != self.updated_at    
    
    def create(self, *args, **kwargs):
        try:
            last_appointment = Appointment.objects.filter(created_at__date=timezone.now()).latest('created_at')
            self.turn = last_appointment.turn + 1
        except Appointment.DoesNotExist:
            self.turn = 1
        super(Appointment, self).save(*args, **kwargs)

    def get_doctors(self):
        return [{'id': doctor.id, 'name': doctor.user.get_full_name()} for doctor in Doctor.objects.all()]

class Emphasis(models.Model):
    name = models.CharField(max_length=255)
    appointment = models.ForeignKey(Appointment, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)