from django.db import models
from exam.models import Tariff
from authentication.models import CompanyUser

class EconomyActivity(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
class CompanyInfo(models.Model):
    user = models.OneToOneField(CompanyUser, on_delete=models.CASCADE)
    nit = models.CharField(max_length=255, unique=True, primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    economy_activity = models.ForeignKey(EconomyActivity, models.DO_NOTHING, blank=True, null=True)
    observations = models.TextField(blank=True, null=True)
    has_limit = models.BooleanField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    # List of companies that the company has a contract with.
    tariff = models.ManyToManyField(Tariff, blank=True)

    def __str__(self):
        return self.nickname + "-" + self.name

class MissionCompany(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(CompanyInfo, models.DO_NOTHING, related_name='company', blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

