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
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Occupation(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class MedicInsurance(models.Model):
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

class Appointment(models.Model):
    photo = models.CharField(max_length=255, blank=True, null=True)
    fingerprint = models.CharField(max_length=255, blank=True, null=True)
    signature = models.CharField(max_length=255, blank=True, null=True)
    patient = models.ForeignKey(Patient, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)
    plan = models.ForeignKey(Plan, models.DO_NOTHING, blank=True, null=True)
    occupation = models.ForeignKey(Occupation, models.DO_NOTHING, blank=True, null=True)
    medic_insurance = models.ForeignKey(MedicInsurance, models.DO_NOTHING, blank=True, null=True)
    pension_fund = models.ForeignKey(PensionFund, models.DO_NOTHING, blank=True, null=True)
    occupation_risk_insurance = models.ForeignKey(OccupationRiskInsurance, models.DO_NOTHING, blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    payment_amount = models.FloatField(blank=True, null=True)
    owed_amount = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    company_section = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    appointment_at = models.DateTimeField(blank=True, null=True)
    mission_company = models.ForeignKey('MissionCompanies', models.DO_NOTHING, blank=True, null=True)
    doctor = models.ForeignKey(Doctor, models.DO_NOTHING, blank=True, null=True)
    city = models.ForeignKey('Cities', models.DO_NOTHING, blank=True, null=True)
    evaluation_type = models.ForeignKey('EvaluationTypes', models.DO_NOTHING, blank=True, null=True)
    profile_picture = models.TextField(blank=True, null=True)
    invoice_id = models.IntegerField(blank=True, null=True)
    invoiced = models.BooleanField(blank=True, null=True)
    order = models.ForeignKey('Orders', models.DO_NOTHING, blank=True, null=True)
    laboratory_state = models.IntegerField(blank=True, null=True)
    payment_type = models.ForeignKey('PaymentTypes', models.DO_NOTHING, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    signature = models.BinaryField(blank=True, null=True)
    observations = models.TextField(blank=True, null=True)
    turn = models.IntegerField(blank=True, null=True)
    package = models.ForeignKey('Packages', models.DO_NOTHING, blank=True, null=True)
    package_price = models.FloatField(blank=True, null=True)
    received_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    medical_record_id = models.IntegerField(blank=True, null=True)


