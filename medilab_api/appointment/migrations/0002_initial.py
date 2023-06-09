# Generated by Django 4.2.2 on 2023-06-20 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('authentication', '0001_initial'),
        ('exam', '0001_initial'),
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receptionistinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.receptionistuser'),
        ),
        migrations.AddField(
            model_name='patientinfo',
            name='marital_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appointment.maritalstatus'),
        ),
        migrations.AddField(
            model_name='patientinfo',
            name='medical_insurance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appointment.medicalinsurance'),
        ),
        migrations.AddField(
            model_name='patientinfo',
            name='occupation_risk_insurance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appointment.occupationriskinsurance'),
        ),
        migrations.AddField(
            model_name='patientinfo',
            name='pension_fund',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appointment.pensionfund'),
        ),
        migrations.AddField(
            model_name='patientinfo',
            name='schooling',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appointment.schooling'),
        ),
        migrations.AddField(
            model_name='patientinfo',
            name='stratum',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appointment.strata'),
        ),
        migrations.AddField(
            model_name='patientinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.patientuser'),
        ),
        migrations.AddField(
            model_name='patientinfo',
            name='zone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appointment.zone'),
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='appointment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appointment.appointment'),
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='appointment.patientinfo'),
        ),
        migrations.AddField(
            model_name='doctorinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.doctoruser'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='exam.city'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='company.companyinfo'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='company_section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appointment.companysection'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appointment.doctorinfo'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='evaluation_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appointment.evaluationtype'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='occupation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appointment.occupation'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='package',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='exam.package'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appointment.patientinfo'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='payment_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appointment.paymenttype'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='registered_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appointment.receptionistinfo'),
        ),
    ]
