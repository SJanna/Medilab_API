from django.contrib.auth.models import AbstractBaseUser, Group, BaseUserManager
from django.db import models


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
    last_login = None
    username = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser


class Gender(models.Model):
    prefix = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    

class IdentificationType(models.Model):
    name = models.CharField(max_length=255)
    prefix = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.prefix} - {self.name}'


class Profile(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    identification_type = models.ForeignKey(
        IdentificationType, on_delete=models.CASCADE, null=True)
    identification_number = models.CharField(
        max_length=255, unique=True, primary_key=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gender = models.ForeignKey(
        Gender, models.DO_NOTHING, blank=True, null=True)

    role = models.ForeignKey(Group, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        abstract = True
        
# This are the different types of users that the system will have.
# --------------------------------------------------------------------------------
class DoctorUser(UserBase, Profile):
    pass        # It could have some basic information about the doctor

class PatientUser(UserBase, Profile):
    pass        # It could have some basic information about the patient

class CompanyUser(UserBase, Profile):
    first_name, last_name, identification_number, identification_type, gender = None, None, None, None, None
            # It could have some basic information about the company
    pass

class BacteriologistUser(UserBase, Profile):
    pass        # It could have some basic information about the bacteriologist


class ReceptionistUser(UserBase, Profile):
    pass        # It could have some basic information about the receptionist


class otherUser(UserBase, Profile):
    pass        # It could have some basic information about the other user...
# --------------------------------------------------------------------------------






















