from django.db import models
from authentication.models import DoctorUser, ReceptionistUser, CompanyUser, PatientUser


class EconomyActivity(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tariff(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # One tariff has many exams.

    def __str__(self):
        return self.name


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


class Exam(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    # One exam belongs to one tariff, related_name allows to access the exams of a tariff.
    tariff = models.ForeignKey(
        Tariff, on_delete=models.CASCADE, related_name='exam')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


# This are the information of the user that is logged in.
# ------------------------------------------------------------------------------
class DoctorInfo(models.Model):
    user = models.OneToOneField(DoctorUser, on_delete=models.CASCADE)
    professional_code = models.CharField(max_length=255, blank=True, null=True)
    resolution_number = models.CharField(max_length=255, blank=True, null=True)
    signature = models.BinaryField(blank=True, null=True)


class CompanyInfo(models.Model):
    user = models.OneToOneField(CompanyUser, on_delete=models.CASCADE)
    nit = models.CharField(max_length=255, unique=True, primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    economy_activity = models.ForeignKey(
        EconomyActivity, models.DO_NOTHING, blank=True, null=True)
    observations = models.TextField(blank=True, null=True)
    has_limit = models.BooleanField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    # List of companies that the company has a contract with.
    tariff = models.ManyToManyField(Tariff, blank=True)

    def __str__(self):
        return self.nickname + "-" + self.name


class PatientInfo(models.Model):
    user = models.OneToOneField(PatientUser, on_delete=models.CASCADE)
    profile_picture = models.TextField(blank=True, null=True)
    fingerprint = models.CharField(max_length=255, blank=True, null=True)
    signature = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.CharField(max_length=255, blank=True, null=True)
    place_of_birth = models.CharField(max_length=255, blank=True, null=True)
    dependant = models.CharField(max_length=255, blank=True, null=True)
    schooling = models.ForeignKey(
        Schooling, models.DO_NOTHING, blank=True, null=True)
    zone = models.ForeignKey(Zone, models.DO_NOTHING, blank=True, null=True)
    stratum = models.ForeignKey(
        Strata, models.DO_NOTHING, blank=True, null=True)
    marital_status = models.ForeignKey(
        MaritalStatus, models.DO_NOTHING, blank=True, null=True)
    blood_type = models.CharField(max_length=255, blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    occupation_risk_insurance = models.ForeignKey(
        OccupationRiskInsurance, models.DO_NOTHING, blank=True, null=True)  # ARL
    pension_fund = models.ForeignKey(
        PensionFund, models.DO_NOTHING, blank=True, null=True)
    medical_insurance = models.ForeignKey(
        MedicalInsurance, models.DO_NOTHING, blank=True, null=True)    # medical insurance = eps


class ReceptionistInfo(models.Model):
    user = models.OneToOneField(ReceptionistUser, on_delete=models.CASCADE)
    pass
# ------------------------------------------------------------------------------


class City(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


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


class Package(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class CompanySection(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Appointment(models.Model):
    # Información del paciente -----------------------------------------
    patient = models.ForeignKey(
        PatientInfo, models.DO_NOTHING, blank=True, null=True)
    # ------------------------------------------------------------------

    # Empresa: (mission company)*
    company = models.ForeignKey(
        CompanyInfo, models.DO_NOTHING, blank=True, null=True)

    # Datos de la recepción --------------------------------------------
    city = models.ForeignKey(
        City, models.DO_NOTHING, blank=True, null=True)
    evaluation_type = models.ForeignKey(
        EvaluationType, models.DO_NOTHING, blank=True, null=True)

    occupation = models.ForeignKey(
        Occupation, models.DO_NOTHING, blank=True, null=True)
    doctor = models.ForeignKey(
        DoctorInfo, models.DO_NOTHING, blank=True, null=True)
    payment_type = models.ForeignKey(
        PaymentType, models.DO_NOTHING, blank=True, null=True)
    turn = models.IntegerField(blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)  # Observations
    company_section = models.ForeignKey(
        CompanySection, models.DO_NOTHING, blank=True, null=True)
    package = models.ForeignKey(
        Package, models.DO_NOTHING, blank=True, null=True)
    # ------------------------------------------------------------------

    # Estado del Examen. -----------------------------------------------
    # 0: Pendiente, 1: En proceso, 2: Finalizado, 3: Cancelado
    status = models.IntegerField(blank=True, null=True)
    # ------------------------------------------------------------------

    # Previsualización de resultados -----------------------------------
    status_exam = models.IntegerField(blank=True, null=True)
    # ------------------------------------------------------------------

    # Factura ----------------------------------------------------------

    # ------------------------------------------------------------------
    exams = models.ForeignKey(Exam, models.DO_NOTHING, blank=True, null=True)
    registered_by = models.ForeignKey(
        ReceptionistInfo, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class MedicalRecord(models.Model):
    patient = models.ForeignKey(
        PatientInfo, on_delete=models.CASCADE, related_name='patient')
    appointment = models.ForeignKey(
        Appointment, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class EmailDomainType(models.Model):
    provider = models.CharField(max_length=255, blank=True, null=True)
    domain = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'email_domain_types'


class ExamPackage(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    package = models.ForeignKey(
        Package, models.DO_NOTHING, related_name='package', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class MissionCompany(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(
        CompanyInfo, models.DO_NOTHING, related_name='company', blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


# This will be a default Exam table that allow the Exams table to consult the price of the default exam
class DefaultExams(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
