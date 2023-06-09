# Generated by Django 4.2.2 on 2023-06-20 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('nit', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('nickname', models.CharField(blank=True, max_length=255, null=True)),
                ('observations', models.TextField(blank=True, null=True)),
                ('has_limit', models.BooleanField(blank=True, null=True)),
                ('balance', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EconomyActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MissionCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('active', models.BooleanField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='company', to='company.companyinfo')),
            ],
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='economy_activity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='company.economyactivity'),
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='tariff',
            field=models.ManyToManyField(blank=True, to='exam.tariff'),
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.companyuser'),
        ),
    ]
