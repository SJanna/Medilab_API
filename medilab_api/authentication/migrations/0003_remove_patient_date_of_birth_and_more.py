# Generated by Django 4.2.1 on 2023-08-12 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_rename_roles_user_rol'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='medical_record_number',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='photo',
        ),
        migrations.AddField(
            model_name='patient',
            name='profile_picture',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(default='2002-05-25'),
            preserve_default=False,
        ),
    ]
