# Generated by Django 4.0.3 on 2022-03-30 01:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UniversityModel',
            new_name='FamousUniversity',
        ),
    ]
