from django.apps import apps
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Group
from django.contrib.auth.signals import user_logged_in
from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver


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
    prefix = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class IdentificationType(models.Model):
    prefix = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Role(Group):
    pass

    def __str__(self):
        return self.name


class Profile(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    identification_type = models.ForeignKey(IdentificationType, on_delete=models.SET_NULL, null=True)
    identification_number = models.CharField(max_length=255, unique=True, primary_key=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=55, blank=True, null=True)
    city = models.CharField(max_length=55, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    gender = models.ForeignKey(Gender, models.SET_NULL, null=True) # Male, Female, Other
    role = models.ForeignKey(Role, models.SET_NULL, null=True) # Doctor, Patient, Company, Bacteriologist, Receptionist, Brigade, Other
    last_login_ip = models.GenericIPAddressField(blank=True, null=True)
    
    class Meta:
        abstract = True


# This are the different types of users that the system will have.
# --------------------------------------------------------------------------------
class DoctorUser(UserBase, Profile):
    pass
    def __str__(self):
        return f'Doctor {self.first_name} {self.last_name}'

class PatientUser(UserBase, Profile):
    pass
    def __str__(self):
        return f'Patient {self.first_name} {self.last_name}'

class CompanyUser(UserBase, Profile):
    first_name, last_name, identification_number, identification_type, gender = None, None, None, None, None
    pass
    def __str__(self): 
        return f'Company {self.first_name} {self.last_name}'

class BacteriologistUser(UserBase, Profile):
    pass
    def __str__(self):
        return f'Bacteriologist {self.first_name} {self.last_name}'

class ReceptionistUser(UserBase, Profile):
    pass
    def __str__(self):
        return f'Receptionist {self.first_name} {self.last_name}'
    
class BrigadeUser(UserBase, Profile):
    pass
    def __str__(self):
        return f'Brigade {self.first_name} {self.last_name}'

class OtherUser(UserBase, Profile):
    pass
    def __str__(self):
        return f'Other {self.first_name} {self.last_name}'      
# --------------------------------------------------------------------------------


# Signals en Django son: funciones que se ejecutan antes o despues de que un modelo se guarde en la base de datos.
# Sirven para ejecutar codigo antes o despues de que un modelo se guarde en la base de datos.

#Signals --------------------------------------------------------------------------------
@receiver(user_logged_in)
def update_last_login_ip(sender, user, request, **kwargs):
    # Obtener todos los modelos que heredan de Profile
    profile_models = [
        model.__name__.lower() for model in apps.get_models() if issubclass(model, Profile)
    ]
    
    # Recorrer los modelos y actualizar la última dirección IP de inicio de sesión
    for model_name in profile_models:
        if hasattr(user, model_name):
            # Obtener el perfil correspondiente al modelo
            profile = getattr(user, model_name)
            # Actualizar la última dirección IP de inicio de sesión
            setattr(profile, 'last_login_ip', request.META.get('REMOTE_ADDR'))
            # Guardar los cambios en el perfil
            profile.save()


# Crea los roles de forma automática en la base de datos si no existen
@receiver(post_migrate)
def create_default_roles(sender, **kwargs):
    ROLES = [
        model.__name__.replace('User','') for model in apps.get_models() if issubclass(model, Profile)
    ]
    for role in ROLES:
        Role.objects.get_or_create(name=role)


# Crea los tipos de identificación de forma automática en la base de datos si no existen
@receiver(post_migrate)
def create_default_identification_types(sender,**kwargs):
    IDENTIFICATION_TYPES = [
        ('Cédula de ciudadanía', 'CC'),
        ('Cédula de extranjería', 'CE'),
        ('Pasaporte', 'PAS'),
        ('Registro civil', 'RC'),
        ('Tarjeta de identidad', 'TI'),
        ('Permiso de Trabajo', 'PT'),
        ('Registro Único Tributario', 'RUT'),
        ('Número de Identificación Tributaria', 'NIT'),
        ('Número de Identificación Personal', 'NIP'),
        ('Número de Identificación de Extranjero', 'NIE'),
    ]
    for name, prefix in IDENTIFICATION_TYPES:
        IdentificationType.objects.get_or_create(name=name, prefix=prefix)


# Crea los géneros de forma automática en la base de datos si no existen
@receiver(post_migrate)
def create_default_genders(sender, **kwargs):
    GENDERS = [
        ('Masculino', 'M'),
        ('Femenino', 'F'),
        ('Otro', 'O'),
    ]
    for name, prefix in GENDERS:
        Gender.objects.get_or_create(name=name, prefix=prefix)


# End Signals --------------------------------------------------------------------------------