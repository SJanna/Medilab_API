# Generated by Django 4.2.4 on 2023-09-17 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BodyPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DeseaseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalConcept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_other_medical_concepts', models.BooleanField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('appointment', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appointment.appointment')),
                ('attended_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VisualSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('close_vision_left_ear_first', models.IntegerField(blank=True, null=True)),
                ('close_vision_left_ear_second', models.IntegerField(blank=True, null=True)),
                ('close_vision_right_ear_first', models.IntegerField(blank=True, null=True)),
                ('close_vision_right_ear_second', models.IntegerField(blank=True, null=True)),
                ('distant_vision_left_ear_first', models.IntegerField(blank=True, null=True)),
                ('distant_vision_left_ear_second', models.IntegerField(blank=True, null=True)),
                ('distant_vision_right_ear_first', models.IntegerField(blank=True, null=True)),
                ('distant_vision_right_ear_second', models.IntegerField(blank=True, null=True)),
                ('has_lenses', models.BooleanField()),
                ('chromatic', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('medical_record', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='medical_record.medicalrecord')),
            ],
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('medical_record', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='medical_record.medicalrecord')),
            ],
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptom_type', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('medical_record', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='medical_record.medicalrecord')),
            ],
        ),
        migrations.CreateModel(
            name='RiskType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('medical_record', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='medical_record.medicalrecord')),
            ],
        ),
        migrations.CreateModel(
            name='Postponed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_postponed_date', models.DateField(blank=True, null=True)),
                ('requirements_to_lift_postponed', models.TextField(blank=True, null=True)),
                ('medical_concept', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='medical_record.medicalconcept')),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('laterality', models.CharField(max_length=255)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('imc_value', models.FloatField(blank=True, null=True)),
                ('imc_description', models.CharField(blank=True, max_length=255, null=True)),
                ('fc', models.IntegerField(blank=True, null=True)),
                ('fr', models.IntegerField(blank=True, null=True)),
                ('temperature', models.FloatField(blank=True, null=True)),
                ('pa', models.IntegerField(blank=True, null=True)),
                ('ta_first', models.IntegerField(blank=True, null=True)),
                ('ta_second', models.IntegerField(blank=True, null=True)),
                ('general_aspect', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('medical_record', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='medical_record.medicalrecord')),
            ],
        ),
        migrations.CreateModel(
            name='PathologicalBackground',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personal', models.BooleanField(blank=True, null=True)),
                ('familiar', models.BooleanField(blank=True, null=True)),
                ('paternal', models.BooleanField(blank=True, null=True)),
                ('maternal', models.BooleanField(blank=True, null=True)),
                ('granpaternal', models.BooleanField(blank=True, null=True)),
                ('granmaternal', models.BooleanField(blank=True, null=True)),
                ('detail', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('desease_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='medical_record.deseasetype')),
                ('medical_record', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='medical_record.medicalrecord')),
            ],
        ),
        migrations.CreateModel(
            name='OcuppationalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turn', models.CharField(max_length=255)),
                ('years_exp', models.CharField(max_length=255)),
                ('occupation_type', models.CharField(max_length=255)),
                ('occupation_description', models.CharField(blank=True, max_length=255, null=True)),
                ('epp_previous_occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('epp_current_occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('epp_use_previous_occupation', models.BooleanField(blank=True, null=True)),
                ('epp_use_current_occupation', models.BooleanField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('medical_record', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='medical_record.medicalrecord')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalRecordRecommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('name', models.TextField()),
                ('general_recommendation', models.TextField(blank=True, null=True)),
                ('company_recommendation', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('medical_record', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='medical_record.medicalrecord')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalRecordBodyPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_anormal', models.BooleanField()),
                ('detail', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('body_part', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='medical_record.bodypart')),
                ('medical_record', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='medical_record.medicalrecord')),
            ],
        ),
        migrations.AddField(
            model_name='medicalconcept',
            name='medical_record',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='medical_record.medicalrecord'),
        ),
        migrations.CreateModel(
            name='LaborInjury',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('injury_type', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('injury_date', models.DateTimeField(blank=True, null=True)),
                ('insurance_reported', models.BooleanField(blank=True, null=True)),
                ('aftermath', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('medical_record', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='medical_record.medicalrecord')),
            ],
        ),
        migrations.CreateModel(
            name='LaborBackground',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('years', models.IntegerField(blank=True, null=True)),
                ('months', models.IntegerField(blank=True, null=True)),
                ('risk_factor_one_id', models.IntegerField(blank=True, null=True)),
                ('risk_factor_two_id', models.IntegerField(blank=True, null=True)),
                ('risk_factor_three_id', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('medical_record', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='medical_record.medicalrecord')),
            ],
        ),
        migrations.CreateModel(
            name='HasRestrictions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restriction_time', models.TextField(blank=True, null=True)),
                ('restriction_detail', models.TextField(blank=True, null=True)),
                ('medical_concept', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='medical_record.medicalconcept')),
            ],
        ),
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smoke_use', models.CharField(blank=True, max_length=255, null=True)),
                ('alcoholism_use', models.CharField(blank=True, max_length=255, null=True)),
                ('alcoholism_frecuency', models.CharField(blank=True, max_length=255, null=True)),
                ('psychotropics_use', models.BooleanField()),
                ('handly_activity', models.BooleanField()),
                ('sport_activity', models.BooleanField()),
                ('sport', models.CharField(blank=True, max_length=255, null=True)),
                ('sport_frecuency', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('medical_record', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='medical_record.medicalrecord')),
            ],
        ),
        migrations.CreateModel(
            name='ExamResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('unit', models.CharField(blank=True, max_length=255, null=True)),
                ('reference_value', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_responsable', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('medical_record', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='medical_record.medicalrecord')),
            ],
        ),
        migrations.CreateModel(
            name='EmphasisInMedicalConcept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('medical_concept', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='medical_record.medicalconcept')),
            ],
        ),
        migrations.CreateModel(
            name='Diagnostic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnostic_type', models.CharField(blank=True, max_length=255, null=True)),
                ('cie_code', models.CharField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('medical_record', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='medical_record.medicalrecord')),
            ],
        ),
    ]
