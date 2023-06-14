from django.contrib.auth.models import AbstractBaseUser, Group, BaseUserManager
from django.db import models
# 'Doctores', 'Empresas', 'Pacientes', 'Recepcionista', 'Bacteriologo'

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('El username debe ser proporcionado')

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

class UserBase(AbstractBaseUser):
    last_login= None
    username = models.CharField(max_length=255, unique=True)
    # password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects= UserManager()

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

class Profile(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    identification_type = models.ForeignKey('IdentificationType', on_delete=models.CASCADE)
    identification_number = models.CharField(max_length=255, unique=True, primary_key=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    role = models.ForeignKey(Group, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        abstract=True


class Doctor(UserBase, Profile):
    professional_code = models.CharField(max_length=255, blank=True, null=True)
    resolution_number = models.CharField(max_length=255, blank=True, null=True)
    signature = models.BinaryField(blank=True, null=True)

class Company(UserBase, Profile):
    first_name,last_name,identification_number,identification_type = None, None, None, None
    nit= models.CharField(max_length=255, unique=True, primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    economy_activity = models.ForeignKey('EconomyActivities', models.DO_NOTHING, blank=True, null=True)
    observations = models.TextField(blank=True, null=True)
    has_limit = models.BooleanField(blank=True, null=True)
    limit_amount = models.FloatField(blank=True, null=True)

class Bacteriologist(UserBase, Profile):
    signature = models.BinaryField(blank=True, null=True)

class Receptionist(UserBase, Profile):
    pass

class otherUser(UserBase, Profile):
    pass

class EconomyActivities(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class IdentificationType(models.Model):
    name = models.CharField(max_length=255)
    prefix = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.prefix} - {self.name}'
# Posible modelo para crear pacientes con usuario