# Generated by Django 4.2.7 on 2023-11-21 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_profile', '0017_certification_is_complete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='projects_name',
        ),
        migrations.AddField(
            model_name='experience',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
