# Generated by Django 4.2.7 on 2023-11-17 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='result',
            field=models.FloatField(blank=True, max_length=4, null=True),
        ),
    ]
