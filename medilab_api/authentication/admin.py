from django.contrib import admin
from .models import Patient, Doctor, User, Role

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(User)
admin.site.register(Role)