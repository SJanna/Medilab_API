# Generated by Django 4.2.4 on 2023-09-17 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ExamPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam', to='exam.exam')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField(blank=True, null=True)),
                ('exams', models.ManyToManyField(blank=True, related_name='exams', to='exam.exam')),
            ],
        ),
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('active', models.BooleanField()),
                ('exams_prices', models.ManyToManyField(blank=True, related_name='exams_prices', to='exam.examprice')),
                ('packages', models.ManyToManyField(blank=True, related_name='packages', to='exam.package')),
            ],
        ),
    ]
