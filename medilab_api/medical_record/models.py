from django.db import models
from appointment.models import Appointment
from authentication.models import Patient, User

class MedicalRecord(models.Model):
    # Datos de la consulta --------------------------------------------------------------------------------------
    # patient = models.ForeignKey(Patient, models.DO_NOTHING, blank=True, null=True)
    appointment = models.OneToOneField(Appointment, models.DO_NOTHING, blank=True, null=True) #OnetoOne?
    # -----------------------------------------------------------------------------------------------------------
    # * General: Información Ocupacional, Antecedentes de Exposición al Riesgo. 
    # * A. laborales: Antecedentes laborales.
    # * A. patológicos: Antecedentes Patológicos.
    # * R. sistemas: Antecedentes de accidentes y enfermedades laborales, Hábitos, Vacunas, Revisión por sistemas.
    # * E. físico: Exámen físico, Sistema Visual, Revisión de las partes del cuerpo.
    # -----------------------------------------------------------------------------------------------------------
    # Concepto Médico (Diagnóstico). ----------------------------------------------------------------------------
    
    # -----------------------------------------------------------------------------------------------------------
    # Otros -----------------------------------------------------------------------------------------------------
    attended_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    # general_recommendation = models.TextField(blank=True, null=True)
    # company_recommendation = models.TextField(blank=True, null=True)
    has_other_medical_concepts = models.BooleanField(blank=True, null=True)
    # -----------------------------------------------------------------------------------------------------------
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

# General -------------------------------------------------------------------------------------------------------
# Información Ocupacional
class OcuppationalInfo(models.Model):
    medical_record = models.OneToOneField(MedicalRecord, models.DO_NOTHING)
    # Información Ocupacional (General) -------------------------------------------------------------------------
    turn = models.CharField(max_length=255) # Diurno, Nocturno, ...
    years_exp = models.CharField(max_length=255)
    occupation_type = models.CharField(max_length=255)
    occupation_description = models.CharField(max_length=255,blank=True, null=True)
    # EPP: Equipo de Protección Personal. --> 'Sugerir en el Front End'
    epp_previous_occupation = models.CharField(max_length=255,blank=True, null=True)
    epp_current_occupation = models.CharField(max_length=255,blank=True, null=True)
    epp_use_previous_occupation = models.BooleanField(blank=True, null=True)
    epp_use_current_occupation = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    
# Antecedentes de Exposición al Riesgo
# Tipo de Exámen de Riesgo y Nombre del Exámen
# Ej: Físico: Ruido; Biológico: Biológico
class RiskType(models.Model):
    medical_record = models.ForeignKey(MedicalRecord, models.DO_NOTHING)
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
# ---------------------------------------------------------------------------------------------------------------
    
# A. laborales --------------------------------------------------------------------------------------------------
# Antecedentes laborales.
class LaborBackground(models.Model):
    medical_record = models.ForeignKey(MedicalRecord, models.DO_NOTHING)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    years = models.IntegerField(blank=True, null=True)
    months = models.IntegerField(blank=True, null=True)
    risk_factor_one_id = models.IntegerField(blank=True, null=True)
    risk_factor_two_id = models.IntegerField(blank=True, null=True)
    risk_factor_three_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

# ---------------------------------------------------------------------------------------------------------------

# A. patológicos ------------------------------------------------------------------------------------------------
# Antecedentes Patológicos.

# Se extrajo el modelo para poder agregar nuevas enfermedades desde el Front.
class DeseaseType(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

        
class PathologicalBackground(models.Model):
    medical_record = models.ForeignKey(MedicalRecord, models.DO_NOTHING)
    desease_type = models.ForeignKey(DeseaseType, models.DO_NOTHING, blank=True, null=True)
    personal = models.BooleanField(blank=True, null=True)
    familiar = models.BooleanField(blank=True, null=True)
    paternal = models.BooleanField(blank=True, null=True)
    maternal = models.BooleanField(blank=True, null=True)
    granpaternal = models.BooleanField(blank=True, null=True)
    granmaternal = models.BooleanField(blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    


# ---------------------------------------------------------------------------------------------------------------

# R. sistemas ---------------------------------------------------------------------------------------------------
# Antecedentes de accidentes y enfermedades laborales 

class LaborInjury(models.Model):
    medical_record = models.ForeignKey(MedicalRecord, models.DO_NOTHING) 
    injury_type = models.CharField(max_length=255) # Solo dos opciones: Accidente Laboral y Enfermedad Laboral.
    description = models.CharField(max_length=255,blank=True, null=True)
    injury_date = models.DateTimeField(blank=True, null=True)
    insurance_reported = models.BooleanField(blank=True, null=True)
    aftermath = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)



# Hábitos
class Habit(models.Model):
    medical_record = models.OneToOneField(MedicalRecord, models.DO_NOTHING)
    smoke_use = models.CharField(max_length=255, blank=True, null=True)
    alcoholism_use = models.CharField(max_length=255, blank=True, null=True)
    alcoholism_frecuency = models.CharField(max_length=255, blank=True, null=True)
    psychotropics_use = models.BooleanField()
    handly_activity = models.BooleanField()
    sport_activity = models.BooleanField()
    sport = models.CharField(max_length=255, blank=True, null=True)
    sport_frecuency = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


        
class Vaccine(models.Model):
    medical_record = models.ForeignKey(MedicalRecord, models.DO_NOTHING)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


# Revisión por sistemas: 
# 'SymptomsType' class deleted.
class Symptom(models.Model):
    medical_record = models.ForeignKey(MedicalRecord, models.DO_NOTHING)
    symptom_type = models.CharField(max_length=250) # Visual, auditivo, endocrino, otro, ...
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


# ---------------------------------------------------------------------------------------------------------------


# E. físico -----------------------------------------------------------------------------------------------------
class PhysicalExam(models.Model):
    medical_record = models.OneToOneField(MedicalRecord, models.DO_NOTHING)
    laterality = models.CharField(max_length=255) # Diestro, Zurdo, Ambidiestro.
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    imc_value = models.FloatField(blank=True, null=True)
    imc_description = models.CharField(max_length=255, blank=True, null=True)
    fc = models.IntegerField(blank=True, null=True)
    fr = models.IntegerField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    pa = models.IntegerField(blank=True, null=True)
    ta_first = models.IntegerField(blank=True, null=True) #ta = tensión arterial
    ta_second = models.IntegerField(blank=True, null=True)
    general_aspect = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
        

class VisualSystem(models.Model):
    medical_record = models.OneToOneField(MedicalRecord, models.DO_NOTHING)
    close_vision_left_ear_first = models.IntegerField(blank=True, null=True)
    close_vision_left_ear_second = models.IntegerField(blank=True, null=True)
    close_vision_right_ear_first = models.IntegerField(blank=True, null=True)
    close_vision_right_ear_second = models.IntegerField(blank=True, null=True)
    distant_vision_left_ear_first = models.IntegerField(blank=True, null=True)
    distant_vision_left_ear_second = models.IntegerField(blank=True, null=True)
    distant_vision_right_ear_first = models.IntegerField(blank=True, null=True)
    distant_vision_right_ear_second = models.IntegerField(blank=True, null=True)
    has_lenses = models.BooleanField()
    chromatic = models.CharField(max_length=255) # 2 opciones: Normal, Anormal.
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    

# Para poderse crear desde el front.
class BodyPart(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


# Revisión de las partes del cuerpo.
class MedicalRecordBodyPart(models.Model):
    medical_record = models.ForeignKey(MedicalRecord, models.DO_NOTHING)
    body_part = models.ForeignKey(BodyPart, models.DO_NOTHING, blank=True, null=True) # <- Possible CharField.
    is_anormal = models.BooleanField()
    detail = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


# ---------------------------------------------------------------------------------------------------------------


# Diagnóstico ---------------------------------------------------------------------------------------------------
# CIE10 - Clasificación Internacional de Enfermades -> JSON List.
class Diagnostic(models.Model):
    medical_record = models.OneToOneField(MedicalRecord, models.DO_NOTHING)
    diagnostic_type = models.CharField(max_length=255, blank=True, null=True)
    cie_code = models.CharField(max_length=500, blank=True, null=True) # Código CIE10. JSON list of codes from Front end.
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class MedicalRecordRecommendation(models.Model):
    medical_record = models.ForeignKey(MedicalRecord, models.DO_NOTHING)
    type = models.CharField(max_length=255)
    name = models.TextField()
    general_recommendation = models.TextField(blank=True, null=True) # Recomendación General.
    company_recommendation = models.TextField(blank=True, null=True) # Recomendación Company.
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
  

# Concepto Médico Básico: Al no seleccionar ningún Emphasis. ----------------------------------------------------
class MedicalConcept(models.Model):
    medical_record = models.OneToOneField(MedicalRecord, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255) #opciones: Sin restricciones para el cargo, Con restricciones para el cargo, Aplazado, No apto, Satisfactorio, No satisfactorio
    description = models.TextField(blank=True, null=True) # option list.
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    
class HasRestrictions(models.Model):
    medical_concept = models.OneToOneField(MedicalConcept, on_delete=models.DO_NOTHING)
    restriction_time = models.TextField(blank=True, null=True)
    restriction_detail = models.TextField(blank=True, null=True)
    

class Postponed(models.Model):
    medical_concept = models.OneToOneField(MedicalConcept, on_delete=models.DO_NOTHING)
    max_postponed_date= models.DateField(blank=True, null=True)
    requirements_to_lift_postponed = models.TextField(blank=True, null=True)
# ----------------------------------------------------------------------------------------------------------------    
    
# Concepto Médico según Emphasis.
# Trabajo en Alturas: Apto, No apto.
# ....
class EmphasisInMedicalConcept(models.Model):
    name = models.CharField(max_length=255) # options:apto, no apto.
    medical_concept = models.ForeignKey(MedicalConcept, models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


# Resultados de exámenes
class ExamResult(models.Model):
    medical_record = models.OneToOneField(MedicalRecord, models.DO_NOTHING)
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=255, blank=True, null=True)
    reference_value = models.TextField(blank=True, null=True)
    is_responsable = models.ForeignKey(User, models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

# ---------------------------------------------------------------------------------------------------------------

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


