from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from .managers import BaseManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, validators=[UnicodeUsernameValidator], unique=True)
    email = models.EmailField(max_length=150, unique=True)
    objects = BaseManager()
    
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    is_varified = models.BooleanField(default=False)
    is_team_member = models.BooleanField(default=False, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    
    auth_token = models.CharField(max_length=300, blank=True, null=True)
    otp_token = models.CharField(max_length=6, blank=True, null=True)
    joined_date = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    class Meta:
        ordering = ['joined_date']
    
    def __str__(self) -> str:
        return self.username


class Skills(models.Model):
    STAGE =(
        ('Basic','Basic'),
        ('Medium','Medium'),
        ('Advanced','Advanced')
        )
    name = models.CharField(max_length=200)
    stage = models.CharField(choices=STAGE, max_length=10, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

class Team_Member(User):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    name = models.CharField(max_length=200)
    phone_number = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='team_member/prof/',default='default/default_team_member_image.png', blank=True, null=True)
    cover_image = models.ImageField(upload_to='team_member/cover/', default='default/default_team_member_cover_image.jpg')
    designation = models.CharField(max_length=200, blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    gender = models.CharField(choices=GENDER, blank=True, null=True, max_length=10)
    
    date_of_birth = models.DateField(blank=True, null=True)
    
    skills = models.ManyToManyField(Skills, blank=True)
    
    def __str__(self) -> str:
        return self.name


class Team_Setting_Config(models.Model):
    setting_no = models.PositiveIntegerField(blank=True, null=True)
    team_title = models.CharField(max_length=500, blank=True, null=True)
    team_designation = models.CharField(max_length=500, blank=True, null=True, default='default/pyteam-c-icon.png')
    team_icon = models.ImageField(upload_to='team/', blank=True, null=True)
    team_logo = models.ImageField(upload_to='team/', blank=True, null=True, default='default/team-c-logo-transparent.png')
    team_email = models.EmailField(max_length=200, blank=True, null=True)
    team_phone_number = models.CharField(max_length=14, blank=True, null=True)
    team_team_start = models.DateField(blank=True, null=True)
    team_address = models.TextField(blank=True, null=True)
    team_address_upazila = models.CharField(max_length=50)
    team_address_district = models.CharField(max_length=50, blank=True, null=True)

class Team_Blog_Slide(models.Model):
    team_setting_config = models.OneToOneField(Team_Setting_Config, on_delete=models.CASCADE)

    slide_image = models.ImageField(upload_to='team/', blank=True, null=True, default='default/slider_bg.jpg')
    slide_title = models.CharField(max_length=800, blank=True, null=True)
    title_first = models.CharField(max_length=100, blank=True, null=True)
    title_second = models.CharField(max_length=100, blank=True, null=True)

class Team_About_Us(models.Model):
    team_setting_config = models.OneToOneField(Team_Setting_Config, on_delete=models.CASCADE)

    team_profile_pic = models.ImageField(upload_to='team/', blank=True, null=True)
    team_college = models.CharField(max_length=300, blank=True, null=True)
    team_short_description = models.TextField(blank=True,null=True)
    team_details_description = models.TextField(blank=True, null=True)

    team_team_clients = models.PositiveIntegerField(blank=True, null=True)
    team_projects = models.PositiveIntegerField(blank=True, null=True)
    team_awards = models.PositiveIntegerField(blank=True, null=True)

class Team_testimonials(models.Model):
    person_name = models.CharField(max_length=300, blank=True, null=True)
    person_designation = models.CharField(max_length=300, blank=True, null=True)
    opinion = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.person_name

class Team_Social_Profiles(models.Model):
    team_setting_config = models.OneToOneField(Team_Setting_Config, on_delete=models.CASCADE)

    website = models.URLField(max_length=200, blank=True, null=True)
    facebook = models.URLField(max_length=200, blank=True, null=True)
    instagram = models.URLField(max_length=200, blank=True, null=True)
    twitter = models.URLField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    github = models.URLField(max_length=200, blank=True, null=True)
    youtube = models.URLField(max_length=200, blank=True, null=True)
    
    def __str__(self) -> str:
        return "Social Profile Link"