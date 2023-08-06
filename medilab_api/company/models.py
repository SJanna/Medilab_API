from django.db import models
from exam.models import Tariff

# Create your models here.
class Company(models.Model):
    economy_activity = models.CharField(max_length=50, blank=True, null=True)
    observations = models.TextField(blank=True, null=True)
    # balance = models.FloatField(blank=True, null=True)
    # has_limit
    tariff = models.ManyToManyField(Tariff, blank=True)
    
class MissionCompany(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING, related_name='company', blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)