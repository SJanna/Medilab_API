from django.db import models
from exam.models import Tariff
from authentication.models import User

# Create your models here.
class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # A company needs a user for credentials authentication.
    nit = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    AKA = models.CharField(max_length=255) # Also Known As, Short Name.
    address = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    observations = models.TextField(blank=True, null=True)
    economy_activity = models.CharField(max_length=255, blank=True, null=True)
    tariff = models.ManyToManyField(Tariff, blank=True)
    # documentos...
    # contactos...
    # balance = models.FloatField(blank=True, null=True)
    # has_limit
    
    
    def __str__(self):
        return self.user.username
    

class MissionCompany(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING, related_name='company', blank=True, null=True)
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    tariff = models.ManyToManyField(Tariff, blank=True)