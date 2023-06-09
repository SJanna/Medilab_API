# Generated by Django 4.2.2 on 2023-06-20 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_remove_bacteriologistuser_last_login_device_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bacteriologistuser',
            name='login_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='brigadeuser',
            name='login_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='companyuser',
            name='login_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='doctoruser',
            name='login_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='otheruser',
            name='login_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='patientuser',
            name='login_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='receptionistuser',
            name='login_count',
            field=models.IntegerField(default=0),
        ),
    ]
