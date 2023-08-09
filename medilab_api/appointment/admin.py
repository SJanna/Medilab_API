from django.contrib import admin

# Register your models here.
from .models import Appointment, Accompanist

admin.site.register(Appointment)
admin.site.register(Accompanist)