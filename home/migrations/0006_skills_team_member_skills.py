# Generated by Django 4.2.7 on 2023-11-17 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_user_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('stage', models.CharField(choices=[('Basic', 'Basic'), ('Medium', 'Medium'), ('Advance', 'Advance')], max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='team_member',
            name='skills',
            field=models.ManyToManyField(blank=True, null=True, to='home.skills'),
        ),
    ]