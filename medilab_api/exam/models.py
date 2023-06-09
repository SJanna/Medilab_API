from django.db import models
# from appointment.models import City

class City(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tariff(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    exams_prices = models.ManyToManyField('ExamPrice', related_name='exams_prices', blank=True) #La lista de examenes(con precio) que tiene el tarifario
    city = models.ForeignKey(City, related_name='city', on_delete=models.CASCADE, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # One tariff has many exams.

    def __str__(self):
        return self.name + ' - ' + self.city.name
    

# Lista de todos los examnes posibles.
class Exam(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Una lista de examenes con un precio
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