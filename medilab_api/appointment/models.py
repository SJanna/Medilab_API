from django.db import models
from authentication.models import Doctor, Company, Patient


class EmailDomainType(models.Model):
    provider = models.CharField(max_length=255, blank=True, null=True)
    domain = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Plan(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(
        Company, models.DO_NOTHING, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Occupation(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class MedicalInsurance(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class PensionFund(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class OccupationRiskInsurance(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Exams(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Appointment(models.Model):
    # Información del paciente
    patient = models.ForeignKey(
        Patient, models.DO_NOTHING, blank=True, null=True)
    # -----------------------------------------------------------------
    # If is a Company => 
    company = models.ForeignKey(
        Company, models.DO_NOTHING, blank=True, null=True)  
    # Company has it's own mission_company. (one or many)
    # Company have its own tariff.
    # -----------------------------------------------------------------
    # Datos de la recepción:
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    city = models.ForeignKey(
        Cities, models.DO_NOTHING, blank=True, null=True)
    evaluation_type = models.ForeignKey(
        EvaluationTypes, models.DO_NOTHING, blank=True, null=True)
    pension_fund = models.ForeignKey(
        PensionFund, models.DO_NOTHING, blank=True, null=True)
    medic_insurance = models.ForeignKey(
        MedicInsurances, models.DO_NOTHING, blank=True, null=True)    # medical insurance = eps
    package = models.ForeignKey(
        Packages, models.DO_NOTHING, blank=True, null=True)
    occupation = models.ForeignKey(
        Occupation, models.DO_NOTHING, blank=True, null=True)
    doctor = models.ForeignKey(
        Doctor, models.DO_NOTHING, blank=True, null=True)
    payment_type = models.ForeignKey(
        PaymentTypes, models.DO_NOTHING, blank=True, null=True)
    occupation_risk_insurance = models.ForeignKey(
        OccupationRiskInsurance, models.DO_NOTHING, blank=True, null=True)  # ARL
    turn = models.IntegerField(blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)  # Observations
    company_section = models.CharField(max_length=255, blank=True, null=True)
    exams = models.ForeignKey(Exams, models.DO_NOTHING, blank=True, null=True)
    plan = models.ForeignKey(Plan, models.DO_NOTHING, blank=True, null=True)
    # -----------------------------------------------------------------

    
    laboratory_state = models.IntegerField(blank=True, null=True)

    status = models.IntegerField(blank=True, null=True)
    signature = models.BinaryField(blank=True, null=True)
    observations = models.TextField(blank=True, null=True)

    package_price = models.FloatField(blank=True, null=True)
    received_by = models.ForeignKey(
        'Users', models.DO_NOTHING, blank=True, null=True)
    medical_record_id = models.IntegerField(blank=True, null=True)

    # invoice_id = models.IntegerField(blank=True, null=True)
    # invoiced = models.BooleanField(blank=True, null=True)
    # payment_amount = models.FloatField(blank=True, null=True) # Only 8 fields diff than 0, created at 2020.
    # owed_amount = models.FloatField(blank=True, null=True)  # All fields 0, except one with -1.