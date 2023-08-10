from django.contrib import admin

# Register your models here.
from .models import (BodyPart, DeseaseType, Diagnostic, ExamResult, Habit,
                     LaborBackground, LaborInjury, MedicalConcept,
                     MedicalRecord, MedicalRecordBodyPart,
                     MedicalRecordRecommendation, OcuppationalInfo,
                     PathologicalBackground, PhysicalExam, RiskType, Symptom,
                     Vaccine, VisualSystem)

admin.site.register(MedicalRecord)
admin.site.register(MedicalRecordBodyPart)
admin.site.register(MedicalRecordRecommendation)
admin.site.register(PhysicalExam)
admin.site.register(ExamResult)
admin.site.register(Diagnostic)
admin.site.register(MedicalConcept)
admin.site.register(Symptom)
admin.site.register(Vaccine)
admin.site.register(BodyPart)
admin.site.register(VisualSystem)
admin.site.register(DeseaseType)
admin.site.register(RiskType)
admin.site.register(PathologicalBackground)
admin.site.register(LaborBackground)
admin.site.register(LaborInjury)
admin.site.register(OcuppationalInfo)
admin.site.register(Habit)




# class HabitAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'created_at', 'updated_at')
#     search_fields = ('name', 'description')
#     list_filter = ('created_at', 'updated_at')
