# Generated by Django 4.2.2 on 2023-08-10 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medical_record', '0006_alter_medicalrecordbodypart_body_part_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalrecord',
            name='company_recommendation',
        ),
        migrations.RemoveField(
            model_name='medicalrecord',
            name='general_recommendation',
        ),
    ]