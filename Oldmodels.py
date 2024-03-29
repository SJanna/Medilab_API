# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ActiveAdminComments(models.Model):
    namespace = models.CharField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    resource_id = models.CharField()
    resource_type = models.CharField()
    author_id = models.IntegerField(blank=True, null=True)
    author_type = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'active_admin_comments'


class AdminUsers(models.Model):
    email = models.CharField(unique=True)
    username = models.CharField(unique=True)
    encrypted_password = models.CharField()
    reset_password_token = models.CharField(unique=True, blank=True, null=True)
    reset_password_sent_at = models.DateTimeField(blank=True, null=True)
    remember_created_at = models.DateTimeField(blank=True, null=True)
    sign_in_count = models.IntegerField()
    current_sign_in_at = models.DateTimeField(blank=True, null=True)
    last_sign_in_at = models.DateTimeField(blank=True, null=True)
    current_sign_in_ip = models.GenericIPAddressField(blank=True, null=True)
    last_sign_in_ip = models.GenericIPAddressField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'admin_users'


class AlcoholismTypes(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'alcoholism_types'


class AppointmentExamResults(models.Model):
    appointment_exam_id = models.IntegerField(blank=True, null=True)
    exam_item_id = models.IntegerField(blank=True, null=True)
    result = models.CharField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'appointment_exam_results'


class AppointmentExams(models.Model):
    appointment = models.ForeignKey('Appointments', models.DO_NOTHING, blank=True, null=True)
    exam = models.ForeignKey('Exams', models.DO_NOTHING, blank=True, null=True)
    package = models.ForeignKey('Packages', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    price = models.FloatField(blank=True, null=True)
    visiometry = models.ForeignKey('Visiometries', models.DO_NOTHING, blank=True, null=True)
    audiometry = models.ForeignKey('Audiometries', models.DO_NOTHING, blank=True, null=True)
    espirometry = models.ForeignKey('Espirometries', models.DO_NOTHING, blank=True, null=True)
    medical_record = models.ForeignKey('MedicalRecords', models.DO_NOTHING, blank=True, null=True)
    appointment_package_id = models.IntegerField(blank=True, null=True)
    is_anormal = models.BooleanField(blank=True, null=True)
    result = models.CharField(blank=True, null=True)
    electrocardiogram = models.ForeignKey('Electrocardiograms', models.DO_NOTHING, blank=True, null=True)
    psicological_test = models.ForeignKey('PsicologicalTests', models.DO_NOTHING, blank=True, null=True)
    x_ray = models.ForeignKey('XRays', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    optometry = models.ForeignKey('Optometries', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appointment_exams'


class AppointmentPackages(models.Model):
    package_id = models.IntegerField(blank=True, null=True)
    appointment_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'appointment_packages'


class Appointments(models.Model):
    attention_time = models.CharField(blank=True, null=True)
    patient = models.ForeignKey('Patients', models.DO_NOTHING, blank=True, null=True)
    patient_photo = models.CharField(blank=True, null=True)
    patient_fingerprint = models.CharField(blank=True, null=True)
    patient_signature = models.CharField(blank=True, null=True)
    company = models.ForeignKey('Companies', models.DO_NOTHING, blank=True, null=True)
    plan = models.ForeignKey('Plans', models.DO_NOTHING, blank=True, null=True)
    occupation = models.ForeignKey('Occupations', models.DO_NOTHING, blank=True, null=True)
    medic_insurance = models.ForeignKey('MedicInsurances', models.DO_NOTHING, blank=True, null=True)
    pension_fund = models.ForeignKey('PensionFunds', models.DO_NOTHING, blank=True, null=True)
    occupation_risk_insurance = models.ForeignKey('OccupationRiskInsurances', models.DO_NOTHING, blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    payment_amount = models.FloatField(blank=True, null=True)
    owed_amount = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    company_section = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    appointment_at = models.DateTimeField(blank=True, null=True)
    mission_company = models.ForeignKey('MissionCompanies', models.DO_NOTHING, blank=True, null=True)
    doctor = models.ForeignKey('Doctors', models.DO_NOTHING, blank=True, null=True)
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
    audiometry = models.ForeignKey('Audiometries', models.DO_NOTHING, blank=True, null=True)
    visiometry = models.ForeignKey('Visiometries', models.DO_NOTHING, blank=True, null=True)
    optometry = models.ForeignKey('Optometries', models.DO_NOTHING, blank=True, null=True)
    espirometry = models.ForeignKey('Espirometries', models.DO_NOTHING, blank=True, null=True)
    electrocardiogram = models.ForeignKey('Electrocardiograms', models.DO_NOTHING, blank=True, null=True)
    psicological_test = models.ForeignKey('PsicologicalTests', models.DO_NOTHING, blank=True, null=True)
    x_ray = models.ForeignKey('XRays', models.DO_NOTHING, blank=True, null=True)
    has_alcoholemy = models.BooleanField(blank=True, null=True)
    has_pshycosensometric = models.BooleanField(blank=True, null=True)
    has_vaccine = models.BooleanField(blank=True, null=True)
    has_laboratory = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appointments'


class AptitudeCertificates(models.Model):
    code = models.CharField(blank=True, null=True)
    observation = models.CharField(blank=True, null=True)
    expedition_date = models.DateField(blank=True, null=True)
    medical_record_id = models.IntegerField(blank=True, null=True)
    medical_concept_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    restriction_postponement_description = models.CharField(blank=True, null=True)
    restriction_validity_count = models.CharField(blank=True, null=True)
    restriction_validity_description = models.CharField(blank=True, null=True)
    maximun_date_lift_postponement = models.CharField(blank=True, null=True)
    necessary_list_postponement = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aptitude_certificates'


class Assignments(models.Model):
    role = models.ForeignKey('Roles', models.DO_NOTHING, blank=True, null=True)
    section = models.ForeignKey('Sections', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'assignments'





class AudiometryDiseases(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'audiometry_diseases'


class AudiometryExtraLabourBackgrounds(models.Model):
    audiometry = models.ForeignKey(Audiometries, models.DO_NOTHING, blank=True, null=True)
    audiometry_habit = models.ForeignKey('AudiometryHabits', models.DO_NOTHING, blank=True, null=True)
    has_habit = models.BooleanField(blank=True, null=True)
    observations = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'audiometry_extra_labour_backgrounds'


class AudiometryHabits(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'audiometry_habits'


class AudiometryOtherBackgrounds(models.Model):
    audiometry = models.ForeignKey(Audiometries, models.DO_NOTHING, blank=True, null=True)
    audiometry_other_habit = models.ForeignKey('AudiometryOtherHabits', models.DO_NOTHING, blank=True, null=True)
    has_other_habit = models.BooleanField(blank=True, null=True)
    observations = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'audiometry_other_backgrounds'


class AudiometryOtherHabits(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'audiometry_other_habits'


class AudiometryOthologicBackgrounds(models.Model):
    audiometry = models.ForeignKey(Audiometries, models.DO_NOTHING, blank=True, null=True)
    audiometry_othologic_event = models.ForeignKey('AudiometryOthologicEvents', models.DO_NOTHING, blank=True, null=True)
    right_ear = models.BooleanField(blank=True, null=True)
    left_ear = models.BooleanField(blank=True, null=True)
    no_event = models.BooleanField(blank=True, null=True)
    yes_event = models.BooleanField(blank=True, null=True)
    observations = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'audiometry_othologic_backgrounds'


class AudiometryOthologicEvents(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'audiometry_othologic_events'


class AudiometryPathologicalBackgrounds(models.Model):
    audiometry = models.ForeignKey(Audiometries, models.DO_NOTHING, blank=True, null=True)
    audiometry_disease = models.ForeignKey(AudiometryDiseases, models.DO_NOTHING, blank=True, null=True)
    has_personal_background = models.BooleanField(blank=True, null=True)
    has_familiar_background = models.BooleanField(blank=True, null=True)
    has_disease = models.BooleanField(blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'audiometry_pathological_backgrounds'


class AudiometryRecommendationTypes(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'audiometry_recommendation_types'


class AudiometryRecommendations(models.Model):
    audiometry = models.ForeignKey(Audiometries, models.DO_NOTHING, blank=True, null=True)
    audiometry_recommendation_type = models.ForeignKey(AudiometryRecommendationTypes, models.DO_NOTHING, blank=True, null=True)
    other_recommendations = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    has_recommendation = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audiometry_recommendations'


class Audits(models.Model):
    auditable_id = models.IntegerField(blank=True, null=True)
    auditable_type = models.CharField(blank=True, null=True)
    associated_id = models.IntegerField(blank=True, null=True)
    associated_type = models.CharField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    user_type = models.CharField(blank=True, null=True)
    username = models.CharField(blank=True, null=True)
    action = models.CharField(blank=True, null=True)
    audited_changes = models.TextField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    comment = models.CharField(blank=True, null=True)
    remote_address = models.CharField(blank=True, null=True)
    request_uuid = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audits'


class BankAccounts(models.Model):
    code = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    account_number = models.CharField(blank=True, null=True)
    account_type = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bank_accounts'


class BodyParts(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'body_parts'


class BodySubparts(models.Model):
    body_part = models.ForeignKey(BodyParts, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    left = models.CharField(blank=True, null=True)
    right = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'body_subparts'


class Chromatics(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'chromatics'


class CieCodes(models.Model):
    code = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cie_codes'


class Cities(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cities'


class Companies(models.Model):
    nit = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    nickname = models.CharField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    email = models.CharField(blank=True, null=True)
    city = models.CharField(blank=True, null=True)
    economy_activity = models.ForeignKey('EconomyActivities', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    observations = models.TextField(blank=True, null=True)
    medical_record_allowed = models.BooleanField(blank=True, null=True)
    complementary_allowed = models.BooleanField(blank=True, null=True)
    laboratory_allowed = models.BooleanField(blank=True, null=True)
    is_blocked = models.BooleanField(blank=True, null=True)
    blocked_date = models.DateField(blank=True, null=True)
    has_limit = models.BooleanField(blank=True, null=True)
    limit_amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'companies'


class Companions(models.Model):
    identification_type = models.ForeignKey('IdentificationTypes', models.DO_NOTHING, blank=True, null=True)
    identification_number = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True)
    relationship = models.CharField(blank=True, null=True)
    type = models.CharField(blank=True, null=True)
    appointment = models.ForeignKey(Appointments, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'companions'


class Contacts(models.Model):
    name = models.CharField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True)
    cellphone = models.CharField(blank=True, null=True)
    email = models.CharField(blank=True, null=True)
    company = models.ForeignKey(Companies, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'contacts'


class CovidSurveys(models.Model):
    appointment_id = models.IntegerField(blank=True, null=True)
    survey_date = models.DateTimeField(blank=True, null=True)
    family_members = models.IntegerField(blank=True, null=True)
    fever_last_7_days = models.BooleanField(blank=True, null=True)
    doctor_appointment = models.BooleanField(blank=True, null=True)
    medicine = models.BooleanField(blank=True, null=True)
    laboratory = models.BooleanField(blank=True, null=True)
    specialist = models.BooleanField(blank=True, null=True)
    incapacity = models.BooleanField(blank=True, null=True)
    no_apply = models.BooleanField(blank=True, null=True)
    covid_contact = models.BooleanField(blank=True, null=True)
    hospital_visit = models.BooleanField(blank=True, null=True)
    covid_test = models.BooleanField(blank=True, null=True)
    covid_test_parents = models.BooleanField(blank=True, null=True)
    arterial_hypertension = models.BooleanField(blank=True, null=True)
    mellitus_diabetes = models.BooleanField(blank=True, null=True)
    chronic_bronchitis = models.BooleanField(blank=True, null=True)
    enphysema_pulmonary = models.BooleanField(blank=True, null=True)
    tuberculosis_pulmonary = models.BooleanField(blank=True, null=True)
    bronchial_asthma = models.BooleanField(blank=True, null=True)
    heart_disease = models.BooleanField(blank=True, null=True)
    receiving_medication = models.BooleanField(blank=True, null=True)
    consume_medications = models.TextField(blank=True, null=True)
    surgery = models.BooleanField(blank=True, null=True)
    surgery_details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'covid_surveys'


class DeseaseTypes(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'desease_types'


class DiagnosticTypes(models.Model):
    code = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'diagnostic_types'


class Diagnostics(models.Model):
    medical_record = models.ForeignKey('MedicalRecords', models.DO_NOTHING, blank=True, null=True)
    diagnostic_type = models.ForeignKey(DiagnosticTypes, models.DO_NOTHING, blank=True, null=True)
    cie_code = models.ForeignKey(CieCodes, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'diagnostics'


class Doctors(models.Model):
    identification_type = models.ForeignKey('IdentificationTypes', models.DO_NOTHING, blank=True, null=True)
    identification_number = models.CharField(blank=True, null=True)
    first_name = models.CharField(blank=True, null=True)
    last_name = models.CharField(blank=True, null=True)
    code = models.CharField(blank=True, null=True)
    professional_code = models.CharField(blank=True, null=True)
    resolution_number = models.CharField(blank=True, null=True)
    signature = models.CharField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    email = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctors'


class Documents(models.Model):
    description = models.CharField(blank=True, null=True)
    file = models.CharField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Companies, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'documents'


class EconomyActivities(models.Model):
    code = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'economy_activities'


class Electrocardiograms(models.Model):
    file = models.CharField(blank=True, null=True)
    observations = models.TextField(blank=True, null=True)
    appointment_exam = models.ForeignKey(AppointmentExams, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    result = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'electrocardiograms'


class EmailDomainTypes(models.Model):
    provider = models.CharField(blank=True, null=True)
    domain = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'email_domain_types'


class Entities(models.Model):
    name = models.CharField(blank=True, null=True)
    nit = models.CharField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    owner = models.CharField(blank=True, null=True)
    accounter = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'entities'


class Espirometries(models.Model):
    medical_record = models.ForeignKey('MedicalRecords', models.DO_NOTHING, blank=True, null=True)
    file = models.CharField(blank=True, null=True)
    observations = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    appointment_exam = models.ForeignKey(AppointmentExams, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    result = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'espirometries'


class EvaluationTypes(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'evaluation_types'


class ExamItems(models.Model):
    exam_id = models.IntegerField(blank=True, null=True)
    exam_item_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    unit = models.CharField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    reference_value = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_responsable = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam_items'


class ExamTypes(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    kind = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam_types'


class Exams(models.Model):
    code = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    service = models.ForeignKey('Services', models.DO_NOTHING, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    exam_type = models.ForeignKey(ExamTypes, models.DO_NOTHING, blank=True, null=True)
    observation = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exams'


class Frecuencies(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'frecuencies'


class Genders(models.Model):
    prefix = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'genders'


class Habits(models.Model):
    medical_record = models.ForeignKey('MedicalRecords', models.DO_NOTHING, blank=True, null=True)
    smoke_type = models.ForeignKey('SmokeTypes', models.DO_NOTHING, blank=True, null=True)
    alcoholism_type = models.ForeignKey(AlcoholismTypes, models.DO_NOTHING, blank=True, null=True)
    alcoholism_frecuency_id = models.IntegerField(blank=True, null=True)
    psichotopics_use = models.CharField(blank=True, null=True)
    handly_activity = models.CharField(blank=True, null=True)
    sport_activity = models.CharField(blank=True, null=True)
    sport = models.CharField(blank=True, null=True)
    sport_frecuency_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'habits'


class Headquarters(models.Model):
    name = models.CharField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    email = models.CharField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True)
    cellphone = models.CharField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    city = models.CharField(blank=True, null=True)
    state = models.CharField(blank=True, null=True)
    country = models.CharField(blank=True, null=True)
    logo = models.CharField(blank=True, null=True)
    slogan = models.CharField(blank=True, null=True)
    entity = models.ForeignKey(Entities, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'headquarters'


class IdentificationTypes(models.Model):
    code = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'identification_types'


class InjuryTypes(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    code = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'injury_types'


class Invoices(models.Model):
    code_number = models.CharField(blank=True, null=True)
    company_id = models.IntegerField(blank=True, null=True)
    mission_company_id = models.IntegerField(blank=True, null=True)
    period_date = models.DateField(blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    paid = models.BooleanField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    city = models.CharField(blank=True, null=True)
    phone_number = models.CharField(blank=True, null=True)
    id_number = models.CharField(blank=True, null=True)
    id_type = models.CharField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    customer = models.CharField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    resolution_id = models.IntegerField(blank=True, null=True)
    bank_account = models.ForeignKey(BankAccounts, models.DO_NOTHING, blank=True, null=True)
    paid_at = models.DateField(blank=True, null=True)
    show_header = models.BooleanField(blank=True, null=True)
    show_signature = models.BooleanField(blank=True, null=True)
    show_stamp = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoices'


class LaborBackgrounds(models.Model):
    medical_record = models.ForeignKey('MedicalRecords', models.DO_NOTHING, blank=True, null=True)
    company_name = models.CharField(blank=True, null=True)
    occupation = models.CharField(blank=True, null=True)
    years = models.IntegerField(blank=True, null=True)
    months = models.IntegerField(blank=True, null=True)
    risk_factor_one_id = models.IntegerField(blank=True, null=True)
    risk_factor_two_id = models.IntegerField(blank=True, null=True)
    risk_factor_three_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'labor_backgrounds'


class LaborInjuries(models.Model):
    medical_record = models.ForeignKey('MedicalRecords', models.DO_NOTHING, blank=True, null=True)
    injury_type = models.ForeignKey(InjuryTypes, models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(blank=True, null=True)
    injury_date = models.DateTimeField(blank=True, null=True)
    insurance_reported = models.BooleanField(blank=True, null=True)
    aftermath = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'labor_injuries'


class MaritalStatuses(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'marital_statuses'


class MedicInsurances(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'medic_insurances'


class MedicalConcepts(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    kind = models.CharField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medical_concepts'


class MedicalRecordBodyParts(models.Model):
    medical_record = models.ForeignKey('MedicalRecords', models.DO_NOTHING, blank=True, null=True)
    body_part = models.ForeignKey(BodyParts, models.DO_NOTHING, blank=True, null=True)
    is_anormal = models.BooleanField(blank=True, null=True)
    detail = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'medical_record_body_parts'


class MedicalRecordOtherMedicalConcepts(models.Model):
    medical_record_id = models.IntegerField(blank=True, null=True)
    other_medical_concept_id = models.IntegerField(blank=True, null=True)
    is_allowed = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'medical_record_other_medical_concepts'


class MedicalRecordRecommendations(models.Model):
    medical_record = models.ForeignKey('MedicalRecords', models.DO_NOTHING, blank=True, null=True)
    recommendation = models.ForeignKey('Recommendations', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'medical_record_recommendations'


class MedicalRecordRisks(models.Model):
    medical_record = models.ForeignKey('MedicalRecords', models.DO_NOTHING, blank=True, null=True)
    risk_subtype = models.ForeignKey('RiskSubtypes', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'medical_record_risks'


class MedicalRecords(models.Model):
    # Datos de la consulta --------------------------------------------------------------------------------------
    patient = models.ForeignKey('Patients', models.DO_NOTHING, blank=True, null=True)
    appointment = models.ForeignKey(Appointments, models.DO_NOTHING, blank=True, null=True)
    evaluation_type = models.ForeignKey(EvaluationTypes, models.DO_NOTHING, blank=True, null=True)
    # -----------------------------------------------------------------------------------------------------------
    # Información Ocupacional (General) -------------------------------------------------------------------------
    occupation_turn = models.ForeignKey('OccupationTurns', models.DO_NOTHING, blank=True, null=True)
    occupation_seniority = models.ForeignKey('OccupationSeniorities', models.DO_NOTHING, blank=True, null=True)
    occupation_type = models.ForeignKey('OccupationTypes', models.DO_NOTHING, blank=True, null=True)
    occupation_description = models.CharField(blank=True, null=True)
    epp_previous_occupation = models.CharField(blank=True, null=True)
    epp_current_occupation = models.CharField(blank=True, null=True)
    epp_use_previous_occupation = models.BooleanField(blank=True, null=True)
    epp_use_current_occupation = models.BooleanField(blank=True, null=True)

    # -----------------------------------------------------------------------------------------------------------
    # Hábitos (R.Sistemas) --------------------------------------------------------------------------------------
    smoke_type = models.ForeignKey('SmokeTypes', models.DO_NOTHING, blank=True, null=True)
    smoking_time = models.CharField(blank=True, null=True)
    cigarettes_numbers = models.IntegerField(blank=True, null=True)
    alcoholism_type = models.ForeignKey(AlcoholismTypes, models.DO_NOTHING, blank=True, null=True)
    alcoholism_frecuency_id = models.IntegerField(blank=True, null=True)
    psichotopics_use = models.CharField(blank=True, null=True)
    handly_activity = models.CharField(blank=True, null=True)
    sport_activity = models.CharField(blank=True, null=True)
    sport = models.CharField(blank=True, null=True)
    sport_frecuency_id = models.IntegerField(blank=True, null=True)
    # -----------------------------------------------------------------------------------------------------------
    # Vacunas (R.Sistemas) --------------------------------------------------------------------------------------
    vaccine_scheme = models.CharField(blank=True, null=True)
    # -----------------------------------------------------------------------------------------------------------
    # Exámen físico (E.Físico) ----------------------------------------------------------------------------------
    laterality = models.CharField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    imc_value = models.FloatField(blank=True, null=True)
    imc_description = models.CharField(blank=True, null=True)
    ta_first = models.IntegerField(blank=True, null=True)
    ta_second = models.IntegerField(blank=True, null=True)
    fc = models.IntegerField(blank=True, null=True)
    fr = models.IntegerField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    pa = models.IntegerField(blank=True, null=True)
    general_aspect = models.CharField(blank=True, null=True)
    blood_type = models.CharField(blank=True, null=True)
    # -----------------------------------------------------------------------------------------------------------
    # Sistema visual (E.Físico) ---------------------------------------------------------------------------------
    close_vision_left_ear_first = models.IntegerField(blank=True, null=True)
    close_vision_left_ear_second = models.IntegerField(blank=True, null=True)
    close_vision_right_ear_first = models.IntegerField(blank=True, null=True)
    close_vision_right_ear_second = models.IntegerField(blank=True, null=True)
    distant_vision_left_ear_first = models.IntegerField(blank=True, null=True)
    distant_vision_left_ear_second = models.IntegerField(blank=True, null=True)
    distant_vision_right_ear_first = models.IntegerField(blank=True, null=True)
    distant_vision_right_ear_second = models.IntegerField(blank=True, null=True)
    has_lenses = models.BooleanField(blank=True, null=True)
    chromatic = models.ForeignKey(Chromatics, models.DO_NOTHING, blank=True, null=True)
    # -----------------------------------------------------------------------------------------------------------
    # Ginecológico (A.Patológico) ----------------------------------------------------------------------------------
    menarche = models.IntegerField(blank=True, null=True)
    cicle_period = models.IntegerField(blank=True, null=True)
    cicle_duration = models.IntegerField(blank=True, null=True)
    cytology = models.BooleanField(blank=True, null=True)
    cytology_result = models.CharField(blank=True, null=True)
    last_cytology_date = models.CharField(blank=True, null=True)
    fum = models.CharField(blank=True, null=True)
    planning = models.BooleanField(blank=True, null=True)
    decrease = models.BooleanField(blank=True, null=True)
    g_parity = models.IntegerField(blank=True, null=True)
    p_parity = models.IntegerField(blank=True, null=True)
    c_parity = models.IntegerField(blank=True, null=True)
    a_parity = models.IntegerField(blank=True, null=True)
    e_parity = models.IntegerField(blank=True, null=True)
    observations = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    planification_method = models.CharField(blank=True, null=True)
    # -----------------------------------------------------------------------------------------------------------
    # Otros -----------------------------------------------------------------------------------------------------
    attended_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    general_recommendation = models.TextField(blank=True, null=True)
    company_recommendation = models.TextField(blank=True, null=True)
    has_other_medical_concepts = models.BooleanField(blank=True, null=True)
    # -----------------------------------------------------------------------------------------------------------
    
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'medical_records'


class MissionCompanies(models.Model):
    nit = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    economy_activity = models.ForeignKey(EconomyActivities, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(Companies, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mission_companies'


class OccupationRiskInsurances(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'occupation_risk_insurances'


class OccupationSeniorities(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'occupation_seniorities'


class OccupationTurns(models.Model):
    code = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'occupation_turns'


class OccupationTypes(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'occupation_types'


class Occupations(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'occupations'


class Optometries(models.Model):
    # Datos de la consulta --------------------------------------------------------------------------------------
    code = models.CharField(blank=True, null=True)
    expedition_date = models.DateField(blank=True, null=True)
    # -----------------------------------------------------------------------------------------------------------
    # Antecedentes ocupacionales ---------------------------------------------------------------------------------
    occupation = models.CharField(blank=True, null=True)
    occupation_time_years = models.IntegerField(blank=True, null=True)
    occupation_time_months = models.IntegerField(blank=True, null=True)
    has_protection = models.CharField(blank=True, null=True)
    what_protection = models.CharField(blank=True, null=True)
    # -----------------------------------------------------------------------------------------------------------
    # Examen agudeza visual anterior -----------------------------------------------------------------------------
    has_previous_test = models.BooleanField(blank=True, null=True)
    last_test_date = models.CharField(blank=True, null=True)
    has_formulated_lenses = models.BooleanField(blank=True, null=True)
    formulated_lenses_since_years = models.IntegerField(blank=True, null=True)
    formulated_lenses_since_months = models.IntegerField(blank=True, null=True)
    last_lenses_change_date = models.CharField(blank=True, null=True)
    currently_use_lenses = models.BooleanField(blank=True, null=True)
    visiometry_correction_type_id = models.IntegerField(blank=True, null=True)
    what_correction = models.CharField(blank=True, null=True)
    has_lens_present = models.BooleanField(blank=True, null=True)
    has_eye_surgery = models.BooleanField(blank=True, null=True)
    what_eye_surgery = models.CharField(blank=True, null=True)
    eye_surgery_date = models.CharField(blank=True, null=True)
    #-------------------------------------------------------------------------------------------------------------
    # Signos y síntomas ------------------------------------------------------------------------------------------
    no_report_symptoms = models.BooleanField(blank=True, null=True)
    # -----------------------------------------------------------------------------------------------------------
    # Aguadeza visual -------------------------------------------------------------------------------------------
    far_view_right_eye_without_correction = models.IntegerField(blank=True, null=True)
    far_view_right_eye_with_correction = models.IntegerField(blank=True, null=True)
    far_view_left_eye_without_correction = models.IntegerField(blank=True, null=True)
    far_view_left_eye_with_correction = models.IntegerField(blank=True, null=True)
    close_view_right_eye_without_correction = models.IntegerField(blank=True, null=True)
    close_view_right_eye_with_correction = models.IntegerField(blank=True, null=True)
    close_view_left_eye_without_correction = models.IntegerField(blank=True, null=True)
    close_view_left_eye_with_correction = models.IntegerField(blank=True, null=True)
    left_eye_result = models.CharField(blank=True, null=True)
    right_eye_result = models.CharField(blank=True, null=True)
    # -----------------------------------------------------------------------------------------------------------
    # Otros datos ------------------------------------------------------------------------------------------------
    other_recommendation = models.TextField(blank=True, null=True)
    referred_to = models.CharField(blank=True, null=True)
    referred_cause = models.CharField(blank=True, null=True)
    appointment_exam_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    result = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    # -----------------------------------------------------------------------------------------------------------
    # Examen externo -------------------------------------------------------------------------------------------
    external_test_right_eye = models.CharField(blank=True, null=True)
    external_test_left_eye = models.CharField(blank=True, null=True)
    # -----------------------------------------------------------------------------------------------------------
    # Cover test ------------------------------------------------------------------------------------------------
    cover_test_far_result = models.CharField(blank=True, null=True)
    cover_test_far_detail = models.CharField(blank=True, null=True)
    cover_test_near_result = models.CharField(blank=True, null=True)
    cover_test_near_detail = models.CharField(blank=True, null=True)
    cover_test_ppc = models.CharField(blank=True, null=True)
    # -----------------------------------------------------------------------------------------------------------
    # Oftalmoscopía ---------------------------------------------------------------------------------------------
    ophthalmoscopy_right_eye_result = models.CharField(blank=True, null=True)
    ophthalmoscopy_right_eye_detail = models.CharField(blank=True, null=True)
    ophthalmoscopy_left_eye_result = models.CharField(blank=True, null=True)
    ophthalmoscopy_leftt_eye_detail = models.CharField(blank=True, null=True)
    # -----------------------------------------------------------------------------------------------------------
    # visión cromática ------------------------------------------------------------------------------------------
    chromatic_view = models.CharField(blank=True, null=True)
    chromatic_number = models.CharField(blank=True, null=True)
    chromatic_text = models.CharField(blank=True, null=True)
    # -----------------------------------------------------------------------------------------------------------
    # Estereopsis -----------------------------------------------------------------------------------------------
    stereopsis_result = models.CharField(blank=True, null=True)
    stereopsis_detail = models.CharField(blank=True, null=True)
    # -----------------------------------------------------------------------------------------------------------
    # Queratometría ---------------------------------------------------------------------------------------------
    keratometry_detail = models.CharField(blank=True, null=True)
    keratometry_right_eye = models.CharField(blank=True, null=True)
    keratometry_left_eye = models.CharField(blank=True, null=True)
    # Retinoscopía ----------------------------------------------------------------------------------------------
    retinoscopy_right_eye = models.CharField(blank=True, null=True)
    retinoscopy_left_eye = models.CharField(blank=True, null=True)
    subjetive_right_eye = models.CharField(blank=True, null=True)
    subjetive_left_eye = models.CharField(blank=True, null=True)
    # -----------------------------------------------------------------------------------------------------------
    # Formula Final ----------------------------------------------------------------------------------------------
    final_formule = models.BooleanField(blank=True, null=True)
    final_formule_right_eye = models.CharField(blank=True, null=True)
    final_formule_left_eye = models.CharField(blank=True, null=True)
    # -----------------------------------------------------------------------------------------------------------
    # Lensometría -----------------------------------------------------------------------------------------------
    lensometry_eyes = models.CharField(blank=True, null=True)
    lensometry_add = models.CharField(blank=True, null=True)
    lens_type = models.CharField(blank=True, null=True)
    # -----------------------------------------------------------------------------------------------------------
    

    class Meta:
        managed = False
        db_table = 'optometries'


class OptometryGlassesUses(models.Model):
    optometry = models.ForeignKey(Optometries, models.DO_NOTHING, blank=True, null=True)
    visiometry_correction_type = models.ForeignKey('VisiometryCorrectionTypes', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'optometry_glasses_uses'


class OptometryRecommendations(models.Model):
    optometry = models.ForeignKey(Optometries, models.DO_NOTHING, blank=True, null=True)
    visiometry_recommendation_type = models.ForeignKey('VisiometryRecommendationTypes', models.DO_NOTHING, blank=True, null=True)
    has_recommendation = models.BooleanField(blank=True, null=True)
    other_recommendations = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'optometry_recommendations'


class OptometrySymptoms(models.Model):
    optometry = models.ForeignKey(Optometries, models.DO_NOTHING, blank=True, null=True)
    visiometry_symptom_type = models.ForeignKey('VisiometrySymptomTypes', models.DO_NOTHING, blank=True, null=True)
    has_symptom = models.BooleanField(blank=True, null=True)
    observations = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'optometry_symptoms'


class OrderExams(models.Model):
    order = models.ForeignKey('Orders', models.DO_NOTHING, blank=True, null=True)
    exam = models.ForeignKey(Exams, models.DO_NOTHING, blank=True, null=True)
    package = models.ForeignKey('Packages', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'order_exams'


class Orders(models.Model):
    code = models.CharField(blank=True, null=True)
    company = models.ForeignKey(Companies, models.DO_NOTHING, blank=True, null=True)
    requester = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    comment = models.TextField(blank=True, null=True)
    arrive_at = models.DateTimeField(blank=True, null=True)
    requester_occupation = models.CharField(blank=True, null=True)
    identification_type = models.ForeignKey(IdentificationTypes, models.DO_NOTHING, blank=True, null=True)
    identification_number = models.CharField(blank=True, null=True)
    first_name = models.CharField(blank=True, null=True)
    middle_name = models.CharField(blank=True, null=True)
    last_name = models.CharField(blank=True, null=True)
    second_surname = models.CharField(blank=True, null=True)
    occupation = models.CharField(blank=True, null=True)
    cellphone = models.CharField(blank=True, null=True)
    city = models.ForeignKey(Cities, models.DO_NOTHING, blank=True, null=True)
    mission_company = models.ForeignKey(MissionCompanies, models.DO_NOTHING, blank=True, null=True)
    evaluation_type = models.ForeignKey(EvaluationTypes, models.DO_NOTHING, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    plan = models.ForeignKey('Plans', models.DO_NOTHING, blank=True, null=True)
    package = models.ForeignKey('Packages', models.DO_NOTHING, blank=True, null=True)
    section = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class OtherMedicalConcepts(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'other_medical_concepts'


class PackageExams(models.Model):
    package = models.ForeignKey('Packages', models.DO_NOTHING, blank=True, null=True)
    exam = models.ForeignKey(Exams, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'package_exams'


class Packages(models.Model):
    name = models.CharField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    code = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'packages'


class PathologicalBackgrounds(models.Model):
    desease_type = models.ForeignKey(DeseaseTypes, models.DO_NOTHING, blank=True, null=True)
    personal = models.BooleanField(blank=True, null=True)
    familiar = models.BooleanField(blank=True, null=True)
    paternal = models.BooleanField(blank=True, null=True)
    maternal = models.BooleanField(blank=True, null=True)
    granpaternal = models.BooleanField(blank=True, null=True)
    granmaternal = models.BooleanField(blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    medical_record = models.ForeignKey(MedicalRecords, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pathological_backgrounds'


class Patients(models.Model):
    identification_type = models.ForeignKey(IdentificationTypes, models.DO_NOTHING, blank=True, null=True)
    identification_number = models.CharField(blank=True, null=True)
    first_name = models.CharField(blank=True, null=True)
    middle_name = models.CharField(blank=True, null=True)
    last_name = models.CharField(blank=True, null=True)
    second_surname = models.CharField(blank=True, null=True)
    gender = models.ForeignKey(Genders, models.DO_NOTHING, blank=True, null=True)
    date_of_birth = models.CharField(blank=True, null=True)
    place_of_birth = models.CharField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    city = models.CharField(blank=True, null=True)
    state = models.CharField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True)
    cellphone = models.CharField(blank=True, null=True)
    email = models.CharField(blank=True, null=True)
    dependant = models.CharField(blank=True, null=True)
    schooling = models.ForeignKey('Schoolings', models.DO_NOTHING, blank=True, null=True)
    zone = models.ForeignKey('Zones', models.DO_NOTHING, blank=True, null=True)
    stratum = models.ForeignKey('Strata', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    marital_status = models.ForeignKey(MaritalStatuses, models.DO_NOTHING, blank=True, null=True)
    email_domain_type = models.ForeignKey(EmailDomainTypes, models.DO_NOTHING, blank=True, null=True)
    blood_type = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patients'


class PaymentTypes(models.Model):
    name = models.CharField(blank=True, null=True)
    is_billable = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'payment_types'


class PensionFunds(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pension_funds'


class Plans(models.Model):
    code = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    company = models.ForeignKey(Companies, models.DO_NOTHING, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'plans'


class PsicologicalTests(models.Model):
    file = models.CharField(blank=True, null=True)
    observations = models.TextField(blank=True, null=True)
    appointment_exam = models.ForeignKey(AppointmentExams, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    result = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'psicological_tests'


class Rates(models.Model):
    plan = models.ForeignKey(Plans, models.DO_NOTHING, blank=True, null=True)
    exam = models.ForeignKey(Exams, models.DO_NOTHING, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    package = models.ForeignKey(Packages, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rates'


class RecommendationTypes(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'recommendation_types'


class Recommendations(models.Model):
    recommendation_type = models.ForeignKey(RecommendationTypes, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'recommendations'


class Resolutions(models.Model):
    code = models.CharField(blank=True, null=True)
    res_date = models.DateField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    min_number = models.IntegerField(blank=True, null=True)
    max_number = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    prefix = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resolutions'


class RiskSubtypes(models.Model):
    risk_type = models.ForeignKey('RiskTypes', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'risk_subtypes'


class RiskTypes(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'risk_types'


class Roles(models.Model):
    name = models.CharField(blank=True, null=True)
    visible = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'roles'


class SchemaMigrations(models.Model):
    version = models.CharField(unique=True)

    class Meta:
        managed = False
        db_table = 'schema_migrations'


class Schoolings(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'schoolings'


class Sections(models.Model):
    prefix = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sections'


class Services(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'services'


class SmokeTypes(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'smoke_types'


class Strata(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'strata'


class SymptomTypes(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'symptom_types'


class Symptoms(models.Model):
    medical_record = models.ForeignKey(MedicalRecords, models.DO_NOTHING, blank=True, null=True)
    symptom_type = models.ForeignKey(SymptomTypes, models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'symptoms'


class Users(models.Model):
    identification_number = models.CharField(blank=True, null=True)
    first_name = models.CharField(blank=True, null=True)
    last_name = models.CharField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True)
    cellphone = models.CharField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    state = models.CharField(blank=True, null=True)
    city = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    email = models.CharField(unique=True)
    username = models.CharField(unique=True)
    encrypted_password = models.CharField()
    reset_password_token = models.CharField(unique=True, blank=True, null=True)
    reset_password_sent_at = models.DateTimeField(blank=True, null=True)
    remember_created_at = models.DateTimeField(blank=True, null=True)
    sign_in_count = models.IntegerField()
    current_sign_in_at = models.DateTimeField(blank=True, null=True)
    last_sign_in_at = models.DateTimeField(blank=True, null=True)
    current_sign_in_ip = models.GenericIPAddressField(blank=True, null=True)
    last_sign_in_ip = models.GenericIPAddressField(blank=True, null=True)
    company = models.ForeignKey(Companies, models.DO_NOTHING, blank=True, null=True)
    doctor = models.ForeignKey(Doctors, models.DO_NOTHING, blank=True, null=True)
    headquarter = models.ForeignKey(Headquarters, models.DO_NOTHING, blank=True, null=True)
    role = models.ForeignKey(Roles, models.DO_NOTHING, blank=True, null=True)
    deactivated = models.BooleanField(blank=True, null=True)
    specialization = models.CharField(blank=True, null=True)
    signature = models.BinaryField(blank=True, null=True)
    profile_picture = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class VaccineTypes(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vaccine_types'


class Vaccines(models.Model):
    medical_record = models.ForeignKey(MedicalRecords, models.DO_NOTHING, blank=True, null=True)
    vaccine_type = models.ForeignKey(VaccineTypes, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vaccines'


class Visiometries(models.Model):
    code = models.CharField(blank=True, null=True)
    expedition_date = models.DateField(blank=True, null=True)
    occupation = models.CharField(blank=True, null=True)
    occupation_time_years = models.IntegerField(blank=True, null=True)
    occupation_time_months = models.IntegerField(blank=True, null=True)
    has_protection = models.CharField(blank=True, null=True)
    what_protection = models.CharField(blank=True, null=True)
    has_previous_test = models.BooleanField(blank=True, null=True)
    last_test_date = models.CharField(blank=True, null=True)
    has_formulated_lenses = models.BooleanField(blank=True, null=True)
    formulated_lenses_since_years = models.IntegerField(blank=True, null=True)
    formulated_lenses_since_months = models.IntegerField(blank=True, null=True)
    last_lenses_change_date = models.CharField(blank=True, null=True)
    currently_use_lenses = models.BooleanField(blank=True, null=True)
    visiometry_correction_type = models.ForeignKey('VisiometryCorrectionTypes', models.DO_NOTHING, blank=True, null=True)
    what_correction = models.CharField(blank=True, null=True)
    has_lens_present = models.BooleanField(blank=True, null=True)
    has_eye_surgery = models.BooleanField(blank=True, null=True)
    what_eye_surgery = models.CharField(blank=True, null=True)
    eye_surgery_date = models.CharField(blank=True, null=True)
    no_report_symptoms = models.BooleanField(blank=True, null=True)
    lensometry_eyes = models.CharField(blank=True, null=True)
    lensometry_add = models.CharField(blank=True, null=True)
    lens_type = models.CharField(blank=True, null=True)
    far_view_right_eye_without_correction = models.IntegerField(blank=True, null=True)
    far_view_right_eye_with_correction = models.IntegerField(blank=True, null=True)
    far_view_left_eye_without_correction = models.IntegerField(blank=True, null=True)
    far_view_left_eye_with_correction = models.IntegerField(blank=True, null=True)
    close_view_right_eye_without_correction = models.IntegerField(blank=True, null=True)
    close_view_right_eye_with_correction = models.IntegerField(blank=True, null=True)
    close_view_left_eye_without_correction = models.IntegerField(blank=True, null=True)
    close_view_left_eye_with_correction = models.IntegerField(blank=True, null=True)
    external_test_right_eye = models.CharField(blank=True, null=True)
    external_test_left_eye = models.CharField(blank=True, null=True)
    cover_test_far_result = models.CharField(blank=True, null=True)
    cover_test_far_detail = models.CharField(blank=True, null=True)
    cover_test_near_result = models.CharField(blank=True, null=True)
    cover_test_near_detail = models.CharField(blank=True, null=True)
    cover_test_ppc = models.CharField(blank=True, null=True)
    ophthalmoscopy_right_eye_result = models.CharField(blank=True, null=True)
    ophthalmoscopy_right_eye_detail = models.CharField(blank=True, null=True)
    ophthalmoscopy_left_eye_result = models.CharField(blank=True, null=True)
    ophthalmoscopy_leftt_eye_detail = models.CharField(blank=True, null=True)
    chromatic_view = models.CharField(blank=True, null=True)
    chromatic_number = models.CharField(blank=True, null=True)
    chromatic_text = models.CharField(blank=True, null=True)
    stereopsis_result = models.CharField(blank=True, null=True)
    stereopsis_detail = models.CharField(blank=True, null=True)
    keratometry_detail = models.CharField(blank=True, null=True)
    keratometry_right_eye = models.CharField(blank=True, null=True)
    keratometry_left_eye = models.CharField(blank=True, null=True)
    other_recommendation = models.TextField(blank=True, null=True)
    referred_to = models.CharField(blank=True, null=True)
    referred_cause = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    medical_record = models.ForeignKey(MedicalRecords, models.DO_NOTHING, blank=True, null=True)
    retinoscopy_right_eye = models.CharField(blank=True, null=True)
    retinoscopy_left_eye = models.CharField(blank=True, null=True)
    subjetive_right_eye = models.CharField(blank=True, null=True)
    subjetive_left_eye = models.CharField(blank=True, null=True)
    final_formule = models.BooleanField(blank=True, null=True)
    final_formule_right_eye = models.CharField(blank=True, null=True)
    final_formule_left_eye = models.CharField(blank=True, null=True)
    appointment_exam = models.ForeignKey(AppointmentExams, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(Users, models.DO_NOTHING, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    left_eye_result = models.CharField(blank=True, null=True)
    right_eye_result = models.CharField(blank=True, null=True)
    result = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visiometries'


class VisiometryCorrectionTypes(models.Model):
    order = models.IntegerField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'visiometry_correction_types'


class VisiometryGlassesUseTypes(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'visiometry_glasses_use_types'


class VisiometryGlassesUses(models.Model):
    visiometry = models.ForeignKey(Visiometries, models.DO_NOTHING, blank=True, null=True)
    visiometry_correction_type = models.ForeignKey(VisiometryCorrectionTypes, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'visiometry_glasses_uses'


class VisiometryRecommendationTypes(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'visiometry_recommendation_types'


class VisiometryRecommendations(models.Model):
    visiometry = models.ForeignKey(Visiometries, models.DO_NOTHING, blank=True, null=True)
    visiometry_recommendation_type = models.ForeignKey(VisiometryRecommendationTypes, models.DO_NOTHING, blank=True, null=True)
    has_recommendation = models.BooleanField(blank=True, null=True)
    other_recommendations = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'visiometry_recommendations'


class VisiometrySymptomTypes(models.Model):
    order = models.IntegerField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'visiometry_symptom_types'


class VisiometrySymptoms(models.Model):
    visiometry = models.ForeignKey(Visiometries, models.DO_NOTHING, blank=True, null=True)
    visiometry_symptom_type = models.ForeignKey(VisiometrySymptomTypes, models.DO_NOTHING, blank=True, null=True)
    has_symptom = models.BooleanField(blank=True, null=True)
    observations = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'visiometry_symptoms'


class XRays(models.Model):
    file = models.CharField(blank=True, null=True)
    observations = models.TextField(blank=True, null=True)
    appointment_exam = models.ForeignKey(AppointmentExams, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey(Users, models.DO_NOTHING, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    result = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'x_rays'


class Zones(models.Model):
    prefix = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'zones'
