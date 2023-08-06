from django.db import models

# Create your models here.
class Tariff(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    exams_prices = models.ManyToManyField('ExamPrice', related_name='exams_prices', blank=True) #La lista de examenes(con precio) que tiene el tarifario
    city = models.CharField(max_length=50)
    active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # One tariff has many exams.

    def __str__(self):
        return self.name + ' - ' + self.city.name
    
# Lista de todos los exámenes posibles.
class Exam(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # reference_value; En vez de tener una clase defaultExams para guardar 
    # los precios de loo examenes por defecto, se puede guardar el precio en
    # esta clase llamándolos valores de referencia.

    def __str__(self):
        return self.name

# Una lista de exámenes con un precio
class Package(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    exams = models.ManyToManyField(Exam, related_name='exams', blank=True) #Cambio
    price = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
# Un examen con un precio.
class ExamPrice(models.Model):
    exam = models.ForeignKey(Exam, related_name='exam', on_delete=models.CASCADE)
    price = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.exam.name + ' - ' + str(self.price)

# This will be a default Exam table that allow the Exams table to consult the price of the default exam
class DefaultExams(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()