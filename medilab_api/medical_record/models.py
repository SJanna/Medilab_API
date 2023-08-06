from django.db import models

class MedicalRecords(models.Model):
    # Datos de la consulta --------------------------------------------------------------------------------------
    patient = models.ForeignKey(Patients, models.DO_NOTHING, blank=True, null=True)
    appointment = models.ForeignKey(Appointments, models.DO_NOTHING, blank=True, null=True)
    evaluation_type = models.ForeignKey(EvaluationTypes, models.DO_NOTHING, blank=True, null=True)
    # -----------------------------------------------------------------------------------------------------------
    # Información Ocupacional (General) -------------------------------------------------------------------------
    occupation_turn = models.ForeignKey('OccupationTurns', models.DO_NOTHING, blank=True, null=True)
    occupation_seniority = models.ForeignKey('OccupationSeniorities', models.DO_NOTHING, blank=True, null=True)
    occupation_type = models.ForeignKey('OccupationTypes', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
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
    class Meta:
        managed = False
        db_table = 'medical_records'


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



class Visiometries(models.Model):
    #Visiometría y Optometría tienen los mismos campos, pero en el front de visiometría se muestran menos campos. 
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