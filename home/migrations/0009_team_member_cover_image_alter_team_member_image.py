# Generated by Django 4.2.7 on 2023-11-17 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_skills_name_alter_skills_stage'),
    ]

    operations = [
        migrations.AddField(
            model_name='team_member',
            name='cover_image',
            field=models.ImageField(default='default/default_team_member_cover_image.jpg', upload_to='team_member/cover/'),
        ),
        migrations.AlterField(
            model_name='team_member',
            name='image',
            field=models.ImageField(blank=True, default='default/default_team_member_image.png', null=True, upload_to='team_member/prof/'),
        ),
    ]
