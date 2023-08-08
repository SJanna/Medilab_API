# from django.db import models
# from medilab_api.appointment.models import Appointment

# from medilab_api.authentication.models import Patient

# class MedicalRecord(models.Model):
#     # Datos de la consulta --------------------------------------------------------------------------------------
#     patient = models.ForeignKey(Patient, models.DO_NOTHING, blank=True, null=True)
#     appointment = models.ForeignKey(Appointment, models.DO_NOTHING, blank=True, null=True)
#     evaluation_type = models.ForeignKey(EvaluationTypes, models.DO_NOTHING, blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
    

#     # -----------------------------------------------------------------------------------------------------------
#     # Hábitos (R.Sistemas) --------------------------------------------------------------------------------------
#     smoke_type = models.ForeignKey('SmokeTypes', models.DO_NOTHING, blank=True, null=True)
#     smoking_time = models.CharField(blank=True, null=True)
#     cigarettes_numbers = models.IntegerField(blank=True, null=True)
#     alcoholism_type = models.ForeignKey(AlcoholismTypes, models.DO_NOTHING, blank=True, null=True)
#     alcoholism_frecuency_id = models.IntegerField(blank=True, null=True)
#     psichotopics_use = models.CharField(blank=True, null=True)
#     handly_activity = models.CharField(blank=True, null=True)
#     sport_activity = models.CharField(blank=True, null=True)
#     sport = models.CharField(blank=True, null=True)
#     sport_frecuency_id = models.IntegerField(blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     # Vacunas (R.Sistemas) --------------------------------------------------------------------------------------
#     vaccine_scheme = models.CharField(blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     # Exámen físico (E.Físico) ----------------------------------------------------------------------------------
#     laterality = models.CharField(blank=True, null=True)
#     height = models.IntegerField(blank=True, null=True)
#     weight = models.IntegerField(blank=True, null=True)
#     imc_value = models.FloatField(blank=True, null=True)
#     imc_description = models.CharField(blank=True, null=True)
#     ta_first = models.IntegerField(blank=True, null=True)
#     ta_second = models.IntegerField(blank=True, null=True)
#     fc = models.IntegerField(blank=True, null=True)
#     fr = models.IntegerField(blank=True, null=True)
#     temperature = models.FloatField(blank=True, null=True)
#     pa = models.IntegerField(blank=True, null=True)
#     general_aspect = models.CharField(blank=True, null=True)
#     blood_type = models.CharField(blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     # Sistema visual (E.Físico) ---------------------------------------------------------------------------------
#     close_vision_left_ear_first = models.IntegerField(blank=True, null=True)
#     close_vision_left_ear_second = models.IntegerField(blank=True, null=True)
#     close_vision_right_ear_first = models.IntegerField(blank=True, null=True)
#     close_vision_right_ear_second = models.IntegerField(blank=True, null=True)
#     distant_vision_left_ear_first = models.IntegerField(blank=True, null=True)
#     distant_vision_left_ear_second = models.IntegerField(blank=True, null=True)
#     distant_vision_right_ear_first = models.IntegerField(blank=True, null=True)
#     distant_vision_right_ear_second = models.IntegerField(blank=True, null=True)
#     has_lenses = models.BooleanField(blank=True, null=True)
#     chromatic = models.ForeignKey(Chromatics, models.DO_NOTHING, blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     # Ginecológico (A.Patológico) ----------------------------------------------------------------------------------
#     menarche = models.IntegerField(blank=True, null=True)
#     cicle_period = models.IntegerField(blank=True, null=True)
#     cicle_duration = models.IntegerField(blank=True, null=True)
#     cytology = models.BooleanField(blank=True, null=True)
#     cytology_result = models.CharField(blank=True, null=True)
#     last_cytology_date = models.CharField(blank=True, null=True)
#     fum = models.CharField(blank=True, null=True)
#     planning = models.BooleanField(blank=True, null=True)
#     decrease = models.BooleanField(blank=True, null=True)
#     g_parity = models.IntegerField(blank=True, null=True)
#     p_parity = models.IntegerField(blank=True, null=True)
#     c_parity = models.IntegerField(blank=True, null=True)
#     a_parity = models.IntegerField(blank=True, null=True)
#     e_parity = models.IntegerField(blank=True, null=True)
#     observations = models.TextField(blank=True, null=True)
#     status = models.IntegerField(blank=True, null=True)
#     planification_method = models.CharField(blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     # Otros -----------------------------------------------------------------------------------------------------
#     attended_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
#     general_recommendation = models.TextField(blank=True, null=True)
#     company_recommendation = models.TextField(blank=True, null=True)
#     has_other_medical_concepts = models.BooleanField(blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     class Meta:
#         managed = False
#         db_table = 'medical_records'

# # General -------------------------------------------------------------------------------------------------------
# # Información Ocupacional
# class OcuppationalInfo(models.Model):
#     # Información Ocupacional (General) -------------------------------------------------------------------------
#     turn = models.CharField(max_length=50, blank=True, null=True) # Diurno, Nocturno, ...
#     years_exp = models.CharField(max_length=50, blank=True, null=True)
#     occupation_type = models.CharField(max_length=50, blank=True, null=True)
#     occupation_description = models.CharField(max_length=250,blank=True, null=True)
#     # EPP: Equipo de Protección Personal. --> 'Sugerir en el Front End'
#     epp_previous_occupation = models.CharField(max_length=250,blank=True, null=True)
#     epp_current_occupation = models.CharField(max_length=250,blank=True, null=True)
#     epp_use_previous_occupation = models.BooleanField(blank=True, null=True)
#     epp_use_current_occupation = models.BooleanField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
    
    
# # Antecedentes de Exposición al Riesgo
# # Tipo de Exámen de Riesgo y Nombre del Exámen
# # Ej: Físico: Ruido; Biológico: Biológico
# class RiskType(models.Model):
#     medical_record = models.ForeignKey(MedicalRecord, models.DO_NOTHING)
#     type = models.CharField(max_length=250)
#     name = models.CharField(max_length=250)

#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
# # ---------------------------------------------------------------------------------------------------------------
    
# # A. laborales --------------------------------------------------------------------------------------------------
# # Antecedentes laborales.
# class LaborBackgrounds(models.Model):
#     medical_record = models.ForeignKey(MedicalRecord, models.DO_NOTHING, blank=True, null=True)
#     company_name = models.CharField(max_length=250, blank=True, null=True)
#     occupation = models.CharField(max_length=250, blank=True, null=True)
#     years = models.IntegerField(blank=True, null=True)
#     months = models.IntegerField(blank=True, null=True)
#     risk_factor_one_id = models.IntegerField(blank=True, null=True)
#     risk_factor_two_id = models.IntegerField(blank=True, null=True)
#     risk_factor_three_id = models.IntegerField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'labor_backgrounds'
# # ---------------------------------------------------------------------------------------------------------------

# # A. patológicos ------------------------------------------------------------------------------------------------
# # Antecedentes Patológicos.

# class DeseaseType(models.Model):
#     name = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'desease_types'
        
        
# class PathologicalBackgrounds(models.Model):
#     medical_record = models.ForeignKey(MedicalRecord, models.DO_NOTHING, blank=True, null=True)
#     desease_type = models.ForeignKey(DeseaseType, models.DO_NOTHING, blank=True, null=True)
#     personal = models.BooleanField(blank=True, null=True)
#     familiar = models.BooleanField(blank=True, null=True)
#     paternal = models.BooleanField(blank=True, null=True)
#     maternal = models.BooleanField(blank=True, null=True)
#     granpaternal = models.BooleanField(blank=True, null=True)
#     granmaternal = models.BooleanField(blank=True, null=True)
#     detail = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
    

#     class Meta:
#         managed = False
#         db_table = 'pathological_backgrounds'


# # ---------------------------------------------------------------------------------------------------------------

# # R. sistemas ---------------------------------------------------------------------------------------------------
# # Antecedentes de accidentes y enfermedades laborales 

# class LaborInjuries(models.Model):
#     medical_record = models.ForeignKey(MedicalRecord, models.DO_NOTHING, blank=True, null=True)
#     injury_type = models.CharField(max_length=250)
#     description = models.CharField(blank=True, null=True)
#     injury_date = models.DateTimeField(blank=True, null=True)
#     insurance_reported = models.BooleanField(blank=True, null=True)
#     aftermath = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'labor_injuries'


# class AlcoholismTypes(models.Model):
#     name = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'alcoholism_types'


# # Hábitos
# class Habits(models.Model):
#     medical_record = models.ForeignKey(MedicalRecord, models.DO_NOTHING, blank=True, null=True)
#     smoke_use = models.CharField(max_length=250)
#     alcoholism_use = models.CharField(max_length=250)
#     alcoholism_frecuency = models.CharField(max_length=50)
#     psychotropics_use = models.BooleanField(blank=True, null=True)
#     handly_activity = models.BooleanField(blank=True, null=True)
#     sport_activity = models.BooleanField(blank=True, null=True)
#     sport = models.CharField(max_length=250, blank=True, null=True)
#     sport_frecuency = models.CharField(max_length=250, blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'habits'
        
        
# class Vaccine(models.Model):
#     medical_record = models.ForeignKey(MedicalRecord, models.DO_NOTHING, blank=True, null=True)
#     name = models.CharField(max_length=250, blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'vaccines'
        

# # Revisión por sistemas: 
# # 'SymptomsType' class deleted.
# class Symptoms(models.Model):
#     medical_record = models.ForeignKey(MedicalRecord, models.DO_NOTHING, blank=True, null=True)
#     symptom_type = models.CharField(max_length=250, blank=True, null=True) # <-
#     description = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'symptoms'


# # ---------------------------------------------------------------------------------------------------------------


# # E. físico -----------------------------------------------------------------------------------------------------
# class PhysicalExam(models.Model):
#     medical_record = models.ForeignKey(MedicalRecord, models.DO_NOTHING, blank=True, null=True)
#     laterality = models.CharField(blank=True, null=True)
#     height = models.IntegerField(blank=True, null=True)
#     weight = models.IntegerField(blank=True, null=True)
#     imc_value = models.FloatField(blank=True, null=True)
#     imc_description = models.CharField(max_length=250, blank=True, null=True)
#     ta_first = models.IntegerField(blank=True, null=True)
#     ta_second = models.IntegerField(blank=True, null=True)
#     fc = models.IntegerField(blank=True, null=True)
#     fr = models.IntegerField(blank=True, null=True)
#     temperature = models.FloatField(blank=True, null=True)
#     pa = models.IntegerField(blank=True, null=True)
#     general_aspect = models.CharField(max_length=250, blank=True, null=True)
    
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
    
# # Normal/Anormal
# class Chromatics(models.Model):
#     name = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'chromatics'
        

# class VisualSystem(models.Model):
#     medical_record = models.ForeignKey(MedicalRecord, models.DO_NOTHING, blank=True, null=True)
#     close_vision_left_ear_first = models.IntegerField(blank=True, null=True)
#     close_vision_left_ear_second = models.IntegerField(blank=True, null=True)
#     close_vision_right_ear_first = models.IntegerField(blank=True, null=True)
#     close_vision_right_ear_second = models.IntegerField(blank=True, null=True)
#     distant_vision_left_ear_first = models.IntegerField(blank=True, null=True)
#     distant_vision_left_ear_second = models.IntegerField(blank=True, null=True)
#     distant_vision_right_ear_first = models.IntegerField(blank=True, null=True)
#     distant_vision_right_ear_second = models.IntegerField(blank=True, null=True)
#     has_lenses = models.BooleanField(blank=True, null=True)
#     chromatic = models.ForeignKey(Chromatics, models.DO_NOTHING, blank=True, null=True)
    

# # Maybe Deleted later......
# class BodyParts(models.Model):
#     name = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     order = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'body_parts'


# # Maybe Deleted later......
# class BodySubparts(models.Model):
#     body_part = models.ForeignKey(BodyParts, models.DO_NOTHING, blank=True, null=True)
#     name = models.CharField(max_length=250, blank=True, null=True)
#     left = models.CharField(max_length=250, blank=True, null=True)
#     right = models.CharField(max_length=250, blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'body_subparts'


# # Revisión de las partes del cuerpo.
# class MedicalRecordBodyParts(models.Model):
#     medical_record = models.ForeignKey(MedicalRecord, models.DO_NOTHING, blank=True, null=True)
#     body_part = models.ForeignKey(BodyParts, models.DO_NOTHING, blank=True, null=True) # <- Possible CharField.
#     is_anormal = models.BooleanField(blank=True, null=True)
#     detail = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'medical_record_body_parts'
# # ---------------------------------------------------------------------------------------------------------------


# # Diagnóstico ---------------------------------------------------------------------------------------------------
# # CIE10 - Clasificación Internacional de Enfermades -> JSON List.
# class Diagnostic(models.Model):
#     medical_record = models.ForeignKey(MedicalRecord, models.DO_NOTHING, blank=True, null=True)
#     diagnostic_type = models.CharField(max_length=250, blank=True, null=True)
#     cie_code = models.CharField(max_length=500, blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'diagnostics'
    

# class MedicalRecordRecommendation(models.Model):
#     medical_record = models.ForeignKey(MedicalRecord, models.DO_NOTHING, blank=True, null=True)
#     type = models.CharField(max_length=250)
#     name = models.CharField(max_length=500)
#     general_recommendation = models.CharField(blank=True, null=True) # Recomendación General.
#     company_recommendation = models.CharField(blank=True, null=True) # Recomendación Company.
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'medical_record_recommendations'
        

# # Concepto Médico.
# class MedicalConcept(models.Model):
#     medical_record = models.ForeignKey(MedicalRecord, models.DO_NOTHING, blank=True, null=True)
#     name = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     kind = models.CharField(max_length=250, blank=True, null=True) # option list.
#     observations = models.TextField(blank=True, null=True) # option list.

#     class Meta:
#         managed = False
#         db_table = 'medical_concepts'


# # Resultados de exámenes
# class ExamResult(models.Model):
#     medical_record = models.ForeignKey(MedicalRecord, models.DO_NOTHING, blank=True, null=True)
#     name = models.CharField(blank=True, null=True)
#     unit = models.CharField(blank=True, null=True)
#     order = models.IntegerField(blank=True, null=True)
#     reference_value = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     is_responsable = models.CharField(max_length=250, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'exam_items'
# # ---------------------------------------------------------------------------------------------------------------

# class Optometry(models.Model):
#     # Datos de la consulta --------------------------------------------------------------------------------------
#     code = models.CharField(blank=True, null=True)
#     expedition_date = models.DateField(blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     # Antecedentes ocupacionales ---------------------------------------------------------------------------------
#     occupation = models.CharField(blank=True, null=True)
#     occupation_time_years = models.IntegerField(blank=True, null=True)
#     occupation_time_months = models.IntegerField(blank=True, null=True)
#     has_protection = models.CharField(blank=True, null=True)
#     what_protection = models.CharField(blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     # Examen agudeza visual anterior -----------------------------------------------------------------------------
#     has_previous_test = models.BooleanField(blank=True, null=True)
#     last_test_date = models.CharField(blank=True, null=True)
#     has_formulated_lenses = models.BooleanField(blank=True, null=True)
#     formulated_lenses_since_years = models.IntegerField(blank=True, null=True)
#     formulated_lenses_since_months = models.IntegerField(blank=True, null=True)
#     last_lenses_change_date = models.CharField(blank=True, null=True)
#     currently_use_lenses = models.BooleanField(blank=True, null=True)
#     visiometry_correction_type_id = models.IntegerField(blank=True, null=True)
#     what_correction = models.CharField(blank=True, null=True)
#     has_lens_present = models.BooleanField(blank=True, null=True)
#     has_eye_surgery = models.BooleanField(blank=True, null=True)
#     what_eye_surgery = models.CharField(blank=True, null=True)
#     eye_surgery_date = models.CharField(blank=True, null=True)
#     #-------------------------------------------------------------------------------------------------------------
#     # Signos y síntomas ------------------------------------------------------------------------------------------
#     no_report_symptoms = models.BooleanField(blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     # Aguadeza visual -------------------------------------------------------------------------------------------
#     far_view_right_eye_without_correction = models.IntegerField(blank=True, null=True)
#     far_view_right_eye_with_correction = models.IntegerField(blank=True, null=True)
#     far_view_left_eye_without_correction = models.IntegerField(blank=True, null=True)
#     far_view_left_eye_with_correction = models.IntegerField(blank=True, null=True)
#     close_view_right_eye_without_correction = models.IntegerField(blank=True, null=True)
#     close_view_right_eye_with_correction = models.IntegerField(blank=True, null=True)
#     close_view_left_eye_without_correction = models.IntegerField(blank=True, null=True)
#     close_view_left_eye_with_correction = models.IntegerField(blank=True, null=True)
#     left_eye_result = models.CharField(blank=True, null=True)
#     right_eye_result = models.CharField(blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     # Lensometría -----------------------------------------------------------------------------------------------
#     lensometry_eyes = models.CharField(blank=True, null=True)
#     lensometry_add = models.CharField(blank=True, null=True)
#     lens_type = models.CharField(blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     # Examen externo --------------------------------------------------------------------------------------------
#     external_test_right_eye = models.CharField(blank=True, null=True)
#     external_test_left_eye = models.CharField(blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     # Cover test ------------------------------------------------------------------------------------------------
#     cover_test_far_result = models.CharField(blank=True, null=True)
#     cover_test_far_detail = models.CharField(blank=True, null=True)
#     cover_test_near_result = models.CharField(blank=True, null=True)
#     cover_test_near_detail = models.CharField(blank=True, null=True)
#     cover_test_ppc = models.CharField(blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     # Oftalmoscopía ---------------------------------------------------------------------------------------------
#     ophthalmoscopy_right_eye_result = models.CharField(blank=True, null=True)
#     ophthalmoscopy_right_eye_detail = models.CharField(blank=True, null=True)
#     ophthalmoscopy_left_eye_result = models.CharField(blank=True, null=True)
#     ophthalmoscopy_leftt_eye_detail = models.CharField(blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     # visión cromática ------------------------------------------------------------------------------------------
#     chromatic_view = models.CharField(blank=True, null=True)
#     chromatic_number = models.CharField(blank=True, null=True)
#     chromatic_text = models.CharField(blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     # Estereopsis -----------------------------------------------------------------------------------------------
#     stereopsis_result = models.CharField(blank=True, null=True)
#     stereopsis_detail = models.CharField(blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     # Queratometría ---------------------------------------------------------------------------------------------
#     keratometry_detail = models.CharField(blank=True, null=True)
#     keratometry_right_eye = models.CharField(blank=True, null=True)
#     keratometry_left_eye = models.CharField(blank=True, null=True)
#     # Retinoscopía ----------------------------------------------------------------------------------------------
#     retinoscopy_right_eye = models.CharField(blank=True, null=True)
#     retinoscopy_left_eye = models.CharField(blank=True, null=True)
#     subjetive_right_eye = models.CharField(blank=True, null=True)
#     subjetive_left_eye = models.CharField(blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     # Formula Final ----------------------------------------------------------------------------------------------
#     final_formule = models.BooleanField(blank=True, null=True)
#     final_formule_right_eye = models.CharField(blank=True, null=True)
#     final_formule_left_eye = models.CharField(blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     # Otros datos -----------------------------------------------------------------------------------------------
#     other_recommendation = models.TextField(blank=True, null=True)
#     referred_to = models.CharField(blank=True, null=True)
#     referred_cause = models.CharField(blank=True, null=True)
#     appointment_exam_id = models.IntegerField(blank=True, null=True)
#     user_id = models.IntegerField(blank=True, null=True)
#     status = models.IntegerField(blank=True, null=True)
#     result = models.BooleanField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     # -----------------------------------------------------------------------------------------------------------
    
#     class Meta:
#         managed = False
#         db_table = 'optometries'


# class Visiometry(models.Model):
#     #Visiometría y Optometría tienen los mismos campos, pero en el front de visiometría se muestran menos campos. 
#     # Datos de la consulta --------------------------------------------------------------------------------------
#     code = models.CharField(blank=True, null=True)
#     expedition_date = models.DateField(blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     # Antecedentes ocupacionales ---------------------------------------------------------------------------------
#     occupation = models.CharField(blank=True, null=True)
#     occupation_time_years = models.IntegerField(blank=True, null=True)
#     occupation_time_months = models.IntegerField(blank=True, null=True)
#     has_protection = models.CharField(blank=True, null=True)
#     what_protection = models.CharField(blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     # Examen agudeza visual anterior -----------------------------------------------------------------------------
#     has_previous_test = models.BooleanField(blank=True, null=True)
#     last_test_date = models.CharField(blank=True, null=True)
#     has_formulated_lenses = models.BooleanField(blank=True, null=True)
#     formulated_lenses_since_years = models.IntegerField(blank=True, null=True)
#     formulated_lenses_since_months = models.IntegerField(blank=True, null=True)
#     last_lenses_change_date = models.CharField(blank=True, null=True)
#     currently_use_lenses = models.BooleanField(blank=True, null=True)
#     visiometry_correction_type_id = models.IntegerField(blank=True, null=True)
#     what_correction = models.CharField(blank=True, null=True)
#     has_lens_present = models.BooleanField(blank=True, null=True)
#     has_eye_surgery = models.BooleanField(blank=True, null=True)
#     what_eye_surgery = models.CharField(blank=True, null=True)
#     eye_surgery_date = models.CharField(blank=True, null=True)
#     #-------------------------------------------------------------------------------------------------------------
#     # Signos y síntomas ------------------------------------------------------------------------------------------
#     no_report_symptoms = models.BooleanField(blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     # Aguadeza visual -------------------------------------------------------------------------------------------
#     far_view_right_eye_without_correction = models.IntegerField(blank=True, null=True)
#     far_view_right_eye_with_correction = models.IntegerField(blank=True, null=True)
#     far_view_left_eye_without_correction = models.IntegerField(blank=True, null=True)
#     far_view_left_eye_with_correction = models.IntegerField(blank=True, null=True)
#     close_view_right_eye_without_correction = models.IntegerField(blank=True, null=True)
#     close_view_right_eye_with_correction = models.IntegerField(blank=True, null=True)
#     close_view_left_eye_without_correction = models.IntegerField(blank=True, null=True)
#     close_view_left_eye_with_correction = models.IntegerField(blank=True, null=True)
#     left_eye_result = models.CharField(blank=True, null=True)
#     right_eye_result = models.CharField(blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     # Lensometría -----------------------------------------------------------------------------------------------
#     lensometry_eyes = models.CharField(blank=True, null=True)
#     lensometry_add = models.CharField(blank=True, null=True)
#     lens_type = models.CharField(blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     # Examen externo --------------------------------------------------------------------------------------------
#     external_test_right_eye = models.CharField(blank=True, null=True)
#     external_test_left_eye = models.CharField(blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     # Cover test ------------------------------------------------------------------------------------------------
#     cover_test_far_result = models.CharField(blank=True, null=True)
#     cover_test_far_detail = models.CharField(blank=True, null=True)
#     cover_test_near_result = models.CharField(blank=True, null=True)
#     cover_test_near_detail = models.CharField(blank=True, null=True)
#     cover_test_ppc = models.CharField(blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     # Oftalmoscopía ---------------------------------------------------------------------------------------------
#     ophthalmoscopy_right_eye_result = models.CharField(blank=True, null=True)
#     ophthalmoscopy_right_eye_detail = models.CharField(blank=True, null=True)
#     ophthalmoscopy_left_eye_result = models.CharField(blank=True, null=True)
#     ophthalmoscopy_leftt_eye_detail = models.CharField(blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     # visión cromática ------------------------------------------------------------------------------------------
#     chromatic_view = models.CharField(blank=True, null=True)
#     chromatic_number = models.CharField(blank=True, null=True)
#     chromatic_text = models.CharField(blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     # Estereopsis -----------------------------------------------------------------------------------------------
#     stereopsis_result = models.CharField(blank=True, null=True)
#     stereopsis_detail = models.CharField(blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     # Queratometría ---------------------------------------------------------------------------------------------
#     keratometry_detail = models.CharField(blank=True, null=True)
#     keratometry_right_eye = models.CharField(blank=True, null=True)
#     keratometry_left_eye = models.CharField(blank=True, null=True)
#     # Retinoscopía ----------------------------------------------------------------------------------------------
#     retinoscopy_right_eye = models.CharField(blank=True, null=True)
#     retinoscopy_left_eye = models.CharField(blank=True, null=True)
#     subjetive_right_eye = models.CharField(blank=True, null=True)
#     subjetive_left_eye = models.CharField(blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     # Formula Final ----------------------------------------------------------------------------------------------
#     final_formule = models.BooleanField(blank=True, null=True)
#     final_formule_right_eye = models.CharField(blank=True, null=True)
#     final_formule_left_eye = models.CharField(blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     # Otros datos -----------------------------------------------------------------------------------------------
#     other_recommendation = models.TextField(blank=True, null=True)
#     referred_to = models.CharField(blank=True, null=True)
#     referred_cause = models.CharField(blank=True, null=True)
#     appointment_exam_id = models.IntegerField(blank=True, null=True)
#     user_id = models.IntegerField(blank=True, null=True)
#     status = models.IntegerField(blank=True, null=True)
#     result = models.BooleanField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     # -----------------------------------------------------------------------------------------------------------

#     class Meta:
#         managed = False
#         db_table = 'visiometries'
        

# class Audiometry(models.Model):
#     medical_record = models.ForeignKey(MedicalRecord, models.DO_NOTHING, blank=True, null=True)
#     code = models.CharField(blank=True, null=True)
    
#     # Antecedentes Ocupacionales --------------------------------------------------------------------------------
#     expedition_date = models.DateField(blank=True, null=True)
#     has_previous_test = models.BooleanField(blank=True, null=True)
#     last_test_date = models.CharField(blank=True, null=True)
#     noise_labour_exposition = models.BooleanField(blank=True, null=True)
#     epa_used = models.BooleanField(blank=True, null=True)
#     epa_type = models.CharField(blank=True, null=True)
#     frequency = models.CharField(blank=True, null=True)
#     call_center = models.BooleanField(blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     # Otoscopia -------------------------------------------------------------------------------------------------
#     right_ear_observations = models.TextField(blank=True, null=True)
#     left_ear_observations = models.TextField(blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     # Umbral ----------------------------------------------------------------------------------------------------
#     right_ear_250 = models.IntegerField(blank=True, null=True)
#     right_ear_500 = models.IntegerField(blank=True, null=True)
#     right_ear_1000 = models.IntegerField(blank=True, null=True)
#     right_ear_2000 = models.IntegerField(blank=True, null=True)
#     right_ear_3000 = models.IntegerField(blank=True, null=True)
#     right_ear_4000 = models.IntegerField(blank=True, null=True)
#     right_ear_6000 = models.IntegerField(blank=True, null=True)
#     right_ear_8000 = models.IntegerField(blank=True, null=True)
#     right_ear_pta = models.FloatField(blank=True, null=True)
#     left_ear_250 = models.IntegerField(blank=True, null=True)
#     left_ear_500 = models.IntegerField(blank=True, null=True)
#     left_ear_1000 = models.IntegerField(blank=True, null=True)
#     left_ear_2000 = models.IntegerField(blank=True, null=True)
#     left_ear_3000 = models.IntegerField(blank=True, null=True)
#     left_ear_4000 = models.IntegerField(blank=True, null=True)
#     left_ear_6000 = models.IntegerField(blank=True, null=True)
#     left_ear_8000 = models.IntegerField(blank=True, null=True)
#     left_ear_pta = models.FloatField(blank=True, null=True)
#     # Observaciones Generales -----------------------------------------------------------------------------------
#     general_observations = models.TextField(blank=True, null=True)
#     # -----------------------------------------------------------------------------------------------------------
#     # chart_image = models.TextField(blank=True, null=True) <-- CHART.
#     other_recommendation = models.TextField(blank=True, null=True)
#     result = models.BooleanField(blank=True, null=True)
#     responsable = models.ForeignKey(Doctor, models.DO_NOTHING, blank=True, null=True)
#     status = models.IntegerField(blank=True, null=True)
    
    
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'audiometries'
        

# class AudiometryRecommendations(models.Model):
#     audiometry = models.ForeignKey(Audiometry, models.DO_NOTHING, blank=True, null=True)
#     name = models.CharField(blank=True, null=True) 
#     other_recommendations = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'audiometry_recommendations'
        

# class Espirometry(models.Model):
#     medical_record = models.ForeignKey(MedicalRecord, models.DO_NOTHING, blank=True, null=True)
#     file = models.CharField(blank=True, null=True)
#     observations = models.TextField(blank=True, null=True)
#     doctor = models.ForeignKey(Doctor, models.DO_NOTHING, blank=True, null=True)
#     status = models.IntegerField(blank=True, null=True)
#     result = models.BooleanField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'espirometries'
        

# class PsicologicalTests(models.Model):
#     file = models.CharField(blank=True, null=True)
#     observations = models.TextField(blank=True, null=True)
#     appointment_exam = models.ForeignKey(AppointmentExams, models.DO_NOTHING, blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
#     status = models.IntegerField(blank=True, null=True)
#     result = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'psicological_tests'


# class XRays(models.Model):
#     medical_record = models.ForeignKey(MedicalRecord, models.DO_NOTHING, blank=True, null=True)
#     file = models.CharField(blank=True, null=True)
#     observations = models.TextField(blank=True, null=True)
#     doctor = models.ForeignKey(Doctor, models.DO_NOTHING, blank=True, null=True)
#     status = models.IntegerField(blank=True, null=True)
#     result = models.BooleanField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'x_rays'


