# Generated by Django 4.2.7 on 2023-11-17 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_team_member_date_of_birth_web_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='web_site',
            name='google_map',
            field=models.URLField(blank=True, null=True),
        ),
    ]
