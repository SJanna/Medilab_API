from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group


class Role(models.Model):
    name = models.CharField(max_length=50)
    # It could be FK too.
    # group = models.OneToOneField(Group, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    roles = models.ForeignKey(
        Role, on_delete=models.CASCADE, blank=True, null=True)
    identification_type = models.CharField(max_length=50,blank=True, null=True)
    identification_number = models.CharField(
        max_length=255, unique=True, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=55, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    last_login_ip = models.GenericIPAddressField(blank=True, null=True)

    def __str__(self):
        return self.username


# Signal to handle adding users to the group associated with their role
@receiver(post_save, sender=User)
def add_user_to_group(sender, instance, **kwargs):
    if instance.roles:
        instance.groups.clear()  # Clear existing groups
        instance.groups.add(instance.roles.group)  # Add to new group


# Signal to create default roles and associated groups
@receiver(post_migrate)
def create_default_roles(sender, **kwargs):
    roles = ['MyAdmin', 'Doctor', 'Patient']
    for role_name in roles:
        role, created = Role.objects.get_or_create(name=role_name)
        if created:
            group, _ = Group.objects.get_or_create(name=role_name)
            role.group = group
            role.save()


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=50,blank=True, null=True)
    license_number = models.CharField(max_length=50,blank=True, null=True)

    # other doctor-specific fields here

    def __str__(self):
        return self.user.username


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    medical_record_number = models.CharField(max_length=50)
    profile_picture = models.TextField(blank=True, null=True)
    fingerprint = models.CharField(max_length=255, blank=True, null=True)
    signature = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.CharField(max_length=255, blank=True, null=True)
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





# @receiver(post_migrate)
# def create_default_roles(sender, **kwargs):
#     roles = ['MyAdmin', 'Doctor', 'Patient']
#     for role_name in roles:
#         Role.objects.get_or_create(name=role_name)
