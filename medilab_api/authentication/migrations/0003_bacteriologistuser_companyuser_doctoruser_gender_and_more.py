# Generated by Django 4.2.1 on 2023-06-18 00:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('authentication', '0002_company_role_doctor_role_alter_userbase_password_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BacteriologistUser',
            fields=[
                ('userbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('identification_number', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('department', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('authentication.userbase', models.Model),
        ),
        migrations.CreateModel(
            name='CompanyUser',
            fields=[
                ('userbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('identification_number', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('department', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('authentication.userbase', models.Model),
        ),
        migrations.CreateModel(
            name='DoctorUser',
            fields=[
                ('userbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('identification_number', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('department', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('authentication.userbase', models.Model),
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PatientUser',
            fields=[
                ('userbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('identification_number', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('department', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('gender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='authentication.gender')),
                ('identification_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.identificationtype')),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='auth.group')),
            ],
            options={
                'abstract': False,
            },
            bases=('authentication.userbase', models.Model),
        ),
        migrations.CreateModel(
            name='ReceptionistUser',
            fields=[
                ('userbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('identification_number', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('department', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('gender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='authentication.gender')),
                ('identification_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.identificationtype')),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='auth.group')),
            ],
            options={
                'abstract': False,
            },
            bases=('authentication.userbase', models.Model),
        ),
        migrations.RemoveField(
            model_name='company',
            name='economy_activity',
        ),
        migrations.RemoveField(
            model_name='company',
            name='role',
        ),
        migrations.RemoveField(
            model_name='company',
            name='userbase_ptr',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='identification_type',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='role',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='userbase_ptr',
        ),
        migrations.RemoveField(
            model_name='receptionist',
            name='identification_type',
        ),
        migrations.RemoveField(
            model_name='receptionist',
            name='role',
        ),
        migrations.RemoveField(
            model_name='receptionist',
            name='userbase_ptr',
        ),
        migrations.RemoveField(
            model_name='otheruser',
            name='state',
        ),
        migrations.AddField(
            model_name='otheruser',
            name='department',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Bacteriologist',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.DeleteModel(
            name='EconomyActivities',
        ),
        migrations.DeleteModel(
            name='Receptionist',
        ),
        migrations.AddField(
            model_name='doctoruser',
            name='gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='authentication.gender'),
        ),
        migrations.AddField(
            model_name='doctoruser',
            name='identification_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.identificationtype'),
        ),
        migrations.AddField(
            model_name='doctoruser',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='auth.group'),
        ),
        migrations.AddField(
            model_name='companyuser',
            name='gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='authentication.gender'),
        ),
        migrations.AddField(
            model_name='companyuser',
            name='identification_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.identificationtype'),
        ),
        migrations.AddField(
            model_name='companyuser',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='auth.group'),
        ),
        migrations.AddField(
            model_name='bacteriologistuser',
            name='gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='authentication.gender'),
        ),
        migrations.AddField(
            model_name='bacteriologistuser',
            name='identification_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.identificationtype'),
        ),
        migrations.AddField(
            model_name='bacteriologistuser',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='auth.group'),
        ),
        migrations.AddField(
            model_name='otheruser',
            name='gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='authentication.gender'),
        ),
    ]
