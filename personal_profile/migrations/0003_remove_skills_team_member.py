# Generated by Django 4.2.7 on 2023-11-17 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal_profile', '0002_education_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skills',
            name='team_member',
        ),
    ]