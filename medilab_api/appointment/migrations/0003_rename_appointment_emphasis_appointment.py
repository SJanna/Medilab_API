# Generated by Django 4.2.4 on 2023-08-19 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_remove_appointment_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emphasis',
            old_name='Appointment',
            new_name='appointment',
        ),
    ]
