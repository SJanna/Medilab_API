# Generated by Django 4.2.2 on 2023-08-16 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('authentication', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accompanist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indentification_type', models.CharField(max_length=55)),
                ('identification', models.CharField(max_length=55)),
                ('name', models.CharField(max_length=55)),
                ('phone', models.CharField(max_length=55)),
                ('email', models.CharField(max_length=55)),
                ('relationship', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turn', models.IntegerField()),
                ('city', models.CharField(max_length=255)),
                ('evaluation_type', models.CharField(max_length=255)),
                ('payment_type', models.CharField(blank=True, max_length=50, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('total_amount', models.FloatField()),
                ('status', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('accompanist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appointment.accompanist')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='company.company')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='authentication.doctor')),
                ('package', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='exam.package')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='authentication.patient')),
                ('registered_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Emphasis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('Appointment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='appointment.appointment')),
            ],
        ),
    ]
