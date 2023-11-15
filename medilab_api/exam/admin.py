from django.contrib import admin

# Register your models here.
from .models import Package, Exam, ExamPrice, AppointmentExam, ExamType

admin.site.register(Package)
admin.site.register(Exam)
admin.site.register(ExamPrice)
admin.site.register(AppointmentExam)
admin.site.register(ExamType)