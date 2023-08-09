from django.contrib import admin

# Register your models here.
from .models import Company, Tariff, MissionCompany

admin.site.register(Company)
admin.site.register(Tariff)
admin.site.register(MissionCompany)