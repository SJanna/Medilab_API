# Generated by Django 4.2.4 on 2023-09-18 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0005_alter_appointment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(default='PENDIENTE', max_length=255),
        ),
    ]
