from django.db import models

class Tariff(models.Model):
    name = models.CharField(max_length=255)
    exams_prices = models.ManyToManyField('ExamPrice', related_name='exams_prices', blank=True) #La lista de examenes(con precio) que tiene el tarifario
    packages = models.ManyToManyField('Package', related_name='packages', blank=True) #La lista de paquetes que tiene el tarifario
    active = models.BooleanField()

    def __str__(self):
        return self.name
    

class ExamType(models.Model):
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255) # Icono de la categoria. Probar con iconos de fontawesome o de material ui

# Lista de todos los exámenes posibles.
class Exam(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(ExamType, related_name='type', on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


    def __str__(self):
        return self.name
    
# Una lista de exámenes con un precio
class Package(models.Model):
    name = models.CharField(max_length=255)
    exams = models.ManyToManyField(Exam, related_name='exams', blank=True) #Cambio
    price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name
    
# Un examen con un precio.
class ExamPrice(models.Model):
    exam = models.ForeignKey(Exam, related_name='exam', on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return self.exam.name + ' - ' + str(self.price)

class AppointmentExam(models.Model):
    exam_price = models.ForeignKey(ExamPrice, related_name='exam_price', on_delete=models.CASCADE)
    request_date = models.DateField()
    completion_date = models.DateField(null=True, blank=True)
    STATES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
        ('results_pending', 'Results Pending'),
    )
    status = models.CharField(max_length=20, choices=STATES, default='pending')
