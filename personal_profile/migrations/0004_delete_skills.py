# Generated by Django 4.2.7 on 2023-11-17 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal_profile', '0003_remove_skills_team_member'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Skills',
        ),
    ]
