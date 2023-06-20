from django.db import models
from authentication.models import DoctorUser, ReceptionistUser, PatientUser
from exam.models import Package, City
from company.models import CompanyInfo


class Schooling(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Zone(models.Model):
    prefix = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Strata(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class MaritalStatus(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class OccupationRiskInsurance(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class PensionFund(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class MedicalInsurance(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


# Información de los distintos tipos de usuario.
class DoctorInfo(models.Model):
    user = models.OneToOneField(DoctorUser, on_delete=models.CASCADE)
    professional_code = models.CharField(max_length=255, blank=True, null=True)
    resolution_number = models.CharField(max_length=255, blank=True, null=True)
    signature = models.BinaryField(blank=True, null=True)


class PatientInfo(models.Model):
    user = models.OneToOneField(PatientUser, on_delete=models.CASCADE)
    profile_picture = models.TextField(blank=True, null=True)
    fingerprint = models.CharField(max_length=255, blank=True, null=True)
    signature = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.CharField(max_length=255, blank=True, null=True)
    place_of_birth = models.CharField(max_length=255, blank=True, null=True)
    dependant = models.CharField(max_length=255, blank=True, null=True)
    schooling = models.ForeignKey(Schooling, models.DO_NOTHING, blank=True, null=True)
    zone = models.ForeignKey(Zone, models.DO_NOTHING, blank=True, null=True)
    stratum = models.ForeignKey(Strata, models.DO_NOTHING, blank=True, null=True)
    marital_status = models.ForeignKey(MaritalStatus, models.DO_NOTHING, blank=True, null=True)
    blood_type = models.CharField(max_length=255, blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    occupation_risk_insurance = models.ForeignKey(OccupationRiskInsurance, models.DO_NOTHING, blank=True, null=True)  # ARL
    pension_fund = models.ForeignKey(PensionFund, models.DO_NOTHING, blank=True, null=True)
    medical_insurance = models.ForeignKey(MedicalInsurance, models.DO_NOTHING, blank=True, null=True) # EPS


class ReceptionistInfo(models.Model):
    user = models.OneToOneField(ReceptionistUser, on_delete=models.CASCADE)


class EvaluationType(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Occupation(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class PaymentType(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    

class CompanySection(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Appointment(models.Model):
    # Información del paciente
    patient = models.ForeignKey(PatientInfo, models.DO_NOTHING, blank=True, null=True)

    # Empresa: (mission company)*
    company = models.ForeignKey(CompanyInfo, models.DO_NOTHING, blank=True, null=True)

    # Datos de la recepción
    city = models.ForeignKey(City, models.DO_NOTHING, blank=True, null=True)
    evaluation_type = models.ForeignKey(EvaluationType, models.DO_NOTHING, blank=True, null=True)
    occupation = models.ForeignKey(Occupation, models.DO_NOTHING, blank=True, null=True)
    doctor = models.ForeignKey(DoctorInfo, models.DO_NOTHING, blank=True, null=True)
    payment_type = models.ForeignKey(PaymentType, models.DO_NOTHING, blank=True, null=True)
    turn = models.IntegerField(blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)  # Observations
    company_section = models.ForeignKey(CompanySection, models.DO_NOTHING, blank=True, null=True)
    package = models.ForeignKey(Package, models.DO_NOTHING, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)  # Estado de la cita --> 0: Pendiente, 1: En proceso, 2: Finalizado, 3: Cancelado
    
    # Factura = models.ForeignKey(Factura, models.DO_NOTHING, blank=True, null=True)
    # tariff = models.ForeignKey(Tariff, models.DO_NOTHING, blank=True, null=True) # No hace falta porque ya está en la tabla de company.
    registered_by = models.ForeignKey(ReceptionistInfo, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class MedicalRecord(models.Model):
    patient = models.ForeignKey(PatientInfo, on_delete=models.CASCADE, related_name='patient')
    appointment = models.ForeignKey(Appointment, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()