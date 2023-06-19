from django.db import migrations
from django.contrib.auth.models import Group

ROLES = ['Doctor', 'Patient', 'Company', 'Bacteriologist', 'Receptionist']

def create_groups(apps, schema_editor):
    for role in ROLES:
        Group.objects.get_or_create(name=role)

class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]
