# Generated by Django 4.2.7 on 2023-11-20 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_team_setting_config_team_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='team_setting_config',
            name='setting_no',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
