from django.contrib import admin
from .models import Doctor, Company, IdentificationType

admin.site.register(Doctor)
admin.site.register(Company)
admin.site.register(IdentificationType)
