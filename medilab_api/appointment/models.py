from django.db import models
from authentication.models import User, Patient, Doctor
from company.models import Company
from exam.models import Package


# Create your models here.
class Appointment(models.Model):
    turn = models.IntegerField(blank=True, null=True)
    # Información del paciente
    patient = models.ForeignKey(Patient, models.DO_NOTHING, blank=True, null=True)
    
    # Información del Médico
    doctor = models.ForeignKey(Doctor, models.DO_NOTHING, blank=True, null=True)
    
    # Empresa: (mission company)*
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)
    
    # Datos de la recepción
    department = models.CharField(max_length=55, blank=True, null=True)
    city = models.CharField(max_length=55, blank=True, null=True) # City where the patient is registered.
    occupation = models.CharField(max_length=50, blank=True, null=True)
    payment_type = models.CharField(max_length=50, blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)  # Observations
    company_section = models.CharField(max_length=50, blank=True, null=True)
    package = models.ForeignKey(Package, models.DO_NOTHING, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    
    registered_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient')
    appointment = models.ForeignKey(Appointment, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
    
    
    