from django.db import models
from home.models import Team_Member

# Create your models here.
class About_Me(models.Model):
    team_member = models.OneToOneField(Team_Member, on_delete=models.CASCADE)
    
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    gender = models.CharField(choices=GENDER, blank=True, null=True, max_length=10)
    short_description = models.TextField(blank=True, null=True)
    details_description = models.TextField(blank=True, null=True)
    resume_description = models.TextField(blank=True, null=True)
    testimonials_description = models.TextField(blank=True, null=True)
    
    address = models.TextField(blank=True, null=True)
    address_upazila = models.CharField(max_length=20, blank=True, null=True)
    address_district = models.CharField(max_length=20, blank=True, null=True)
    address_country = models.CharField(max_length=30, default="Bangladesh")
    
    clients = models.PositiveIntegerField(blank=True, null=True)
    projects = models.PositiveIntegerField(blank=True, null=True)
    hours = models.PositiveIntegerField(blank=True, null=True)
    awards = models.PositiveIntegerField(blank=True, null=True)
    
    def __str__(self) -> str:
        return f'About Me - {self.team_member}'




class Web_Site(models.Model):
    team_member = models.OneToOneField(Team_Member, on_delete=models.CASCADE)

    website = models.URLField(max_length=200, blank=True, null=True)
    facebook = models.URLField(max_length=200, blank=True, null=True)
    instagram = models.URLField(max_length=200, blank=True, null=True)
    twitter = models.URLField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    github = models.URLField(max_length=200, blank=True, null=True)
    youtube = models.URLField(max_length=200, blank=True, null=True)
    
    def __str__(self) -> str:
        return f'Social Profile Website Link - {self.team_member}'

class Education(models.Model):
    Degree = (
        ('SSC','SSC'),
        ('HSC','HSC'),
        ('Diploma','Diploma'),
        ('BSC','BSC'),
        ('Other','Other'),
    )
    team_member = models.ForeignKey(Team_Member, on_delete=models.CASCADE)
    
    degree_name = models.CharField(max_length=25, choices=Degree)
    subject = models.CharField(max_length=50, blank=True, null=True)
    result = models.FloatField(max_length=4, blank=True, null=True)
    institute_name = models.CharField(max_length=200)
    institute_address = models.TextField(blank=True, null=True)
    starting_date = models.DateField(blank=True, null=True)
    ending_date = models.DateField(blank=True, null=True)
    duration = models.CharField(max_length=10, blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    is_complete = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.degree_name} - {self.team_member}'

class Certification(models.Model):
    team_member = models.ForeignKey(Team_Member, on_delete=models.CASCADE)
    
    course_name = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=4, blank=True, null=True)
    institute_name = models.CharField(max_length=200)
    institute_address = models.TextField(blank=True, null=True)
    starting_date = models.DateField(blank=True, null=True)
    ending_date = models.DateField(blank=True, null=True)
    duration = models.CharField(max_length=10, blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    
    is_complete = models.BooleanField(default=True, null=False, blank=False)

    def __str__(self) -> str:
        return f'{self.course_name} - {self.team_member}'


class Experience(models.Model):
    team_member = models.ForeignKey(Team_Member, on_delete=models.CASCADE)
    post_name = models.CharField(max_length=30)
    company_name = models.CharField(max_length=40)
    starting_date = models.DateField(blank=True, null=True)
    ending_date = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True, default=True)

    def __str__(self) -> str:
        return f'{self.post_name} - {self.team_member}'


class Portfolio_Category(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title



class Portfolio(models.Model):
    team_member = models.ForeignKey(Team_Member, on_delete=models.CASCADE)
    portfolio_category = models.ForeignKey(Portfolio_Category, on_delete=models.CASCADE, blank=True, null=True)
    
    title = models.CharField(max_length=3000)
    portfolio_image = models.ImageField(upload_to='portfolio/profil_pic/', default='default/default_portfoli_image.jpg', blank=True, null=True)
    portfolio_cover_image = models.ImageField(upload_to='portfolio/cover_pic/', blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    link =  models.URLField()
    is_active = models.BooleanField(default=True, blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.title} - {self.team_member}'



class Testimonials(models.Model):
    team_member = models.ForeignKey(Team_Member, on_delete=models.CASCADE)
    
    person_name = models.CharField(max_length=300, blank=True, null=True)
    person_image = models.ImageField(upload_to='team_member/testimonials/', default='default/personal_profile_tetimonial_icon.png', blank=True, null=True)
    person_designation = models.CharField(max_length=300, blank=True, null=True)
    opinion = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.person_name} - {self.team_member}'