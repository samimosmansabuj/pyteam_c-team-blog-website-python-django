# Generated by Django 4.2.7 on 2023-11-23 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_profile', '0020_remove_about_me_hours'),
    ]

    operations = [
        migrations.AddField(
            model_name='about_me',
            name='hours',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]