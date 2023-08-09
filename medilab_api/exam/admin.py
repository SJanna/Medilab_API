from django.contrib import admin

# Register your models here.
from .models import Package, Exam, ExamPrice

admin.site.register(Package)
admin.site.register(Exam)
admin.site.register(ExamPrice)