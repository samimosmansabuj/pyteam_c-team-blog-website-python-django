# Generated by Django 4.2.7 on 2023-11-18 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_remove_web_site_google_map'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team_About_Us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_profile_pic', models.ImageField(blank=True, null=True, upload_to='team/')),
                ('team_phone_number', models.CharField(blank=True, max_length=14, null=True)),
                ('team_college', models.CharField(blank=True, max_length=300, null=True)),
                ('team_short_description', models.TextField(blank=True, null=True)),
                ('team_details_description', models.TextField(blank=True, null=True)),
                ('team_team_clients', models.PositiveIntegerField(blank=True, null=True)),
                ('team_projects', models.PositiveIntegerField(blank=True, null=True)),
                ('team_awards', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team_Blog_Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slide_image', models.ImageField(blank=True, null=True, upload_to='team/')),
                ('slide_title', models.CharField(blank=True, max_length=800, null=True)),
                ('title_first', models.CharField(blank=True, max_length=100, null=True)),
                ('title_second', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team_Setting_Config',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_title', models.CharField(blank=True, max_length=500, null=True)),
                ('team_designation', models.CharField(blank=True, max_length=500, null=True)),
                ('team_icon', models.ImageField(blank=True, null=True, upload_to='team/')),
                ('team_email', models.EmailField(blank=True, max_length=200, null=True)),
                ('team_team_start', models.DateField(blank=True, null=True)),
                ('team_address', models.TextField(blank=True, null=True)),
                ('team_address_upazila', models.CharField(max_length=50)),
                ('team_address_district', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team_Social_Profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField(blank=True, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('youtube', models.URLField(blank=True, null=True)),
                ('team_setting_config', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.team_setting_config')),
            ],
        ),
        migrations.CreateModel(
            name='Team_testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(blank=True, max_length=300, null=True)),
                ('person_designation', models.CharField(blank=True, max_length=300, null=True)),
                ('opinion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='team_member',
            name='skills',
            field=models.ManyToManyField(to='home.skills'),
        ),
        migrations.DeleteModel(
            name='Web_Site',
        ),
        migrations.AddField(
            model_name='team_blog_slide',
            name='team_setting_config',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.team_setting_config'),
        ),
        migrations.AddField(
            model_name='team_about_us',
            name='team_setting_config',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.team_setting_config'),
        ),
    ]