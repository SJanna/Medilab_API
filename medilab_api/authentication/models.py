from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


class Role(models.Model):
    name = models.CharField(max_length=50)
    # It could be FK too.
    # group = models.OneToOneField(Group, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    roles = models.ForeignKey(
        Role, on_delete=models.CASCADE)
    identification_type = models.CharField(max_length=50)
    identification_number = models.CharField(
        max_length=255, unique=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255)
    department = models.CharField(max_length=55, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    last_login_ip = models.GenericIPAddressField(blank=True, null=True)
    groups, user_permissions = None, None

    def __str__(self):
        return self.username


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=50,blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    professional_code = models.CharField(max_length=255, blank=True, null=True)
    resolution_number = models.CharField(max_length=255, blank=True, null=True)
    signature = models.CharField(max_length=255,blank=True, null=True)

    def __str__(self):
        return self.user.username


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    medical_record_number = models.CharField(max_length=50)
    # profile_picture = models.TextField(blank=True, null=True)
    fingerprint = models.CharField(max_length=255, blank=True, null=True)
    signature = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=255, blank=True, null=True)
    dependant = models.CharField(max_length=255, blank=True, null=True)
    schooling = models.CharField(max_length=50,blank=True, null=True)
    zone = models.CharField(max_length=50,blank=True, null=True)
    stratum = models.CharField(max_length=50,blank=True, null=True)
    marital_status = models.CharField(max_length=50,blank=True, null=True)
    blood_type = models.CharField(max_length=255, blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    occupation_risk_insurance = models.CharField(max_length=50, blank=True, null=True)  # ARL
    pension_fund = models.CharField(max_length=50, blank=True, null=True)
    medical_insurance = models.CharField(max_length=50, blank=True, null=True)  # EPS

    # other patient-specific fields here

    def __str__(self):
        return self.user.username





@receiver(post_migrate)
def create_default_roles(sender, **kwargs):
    roles = ['Admin', 'Doctor', 'Patient']
    for role_name in roles:
        Role.objects.get_or_create(name=role_name)
