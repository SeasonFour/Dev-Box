from django.db import models
# Create your models here.
class DevBoxUser(models.Model):
    user_name = models.CharField(max_length=50,blank=True)
    first_name = models.CharField(max_length=50,blank=False)
    last_name = models.CharField(max_length=50,blank=False)
    email_address = models.EmailField(max_length=50,blank=False)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True

class DevBoxCreatedAt(models.Model):
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True

class Employer(DevBoxUser):
    company_name = models.CharField(max_length=50,blank=True)
    location = models.CharField(max_length=50,blank=True)
    is_employer = models.BooleanField(default=False)

class JobPost(DevBoxCreatedAt):
    title = models.CharField(max_length=50,blank=False)
    description = models.TextField(blank=False)
    skills_required = models.CharField(max_length=50,blank=False)
    location =  models.CharField(max_length=50,blank=False)
    employer = models.ForeignKey(Employer)

class Application(DevBoxCreatedAt):
    applicant_names =  models.CharField(max_length=50,blank=False)
    applicant_location =  models.CharField(max_length=50,blank=False)
    applicant_skills =  models.CharField(max_length=50,blank=False)
    portfolio_link =  models.URLField(max_length=50,blank=False)
    application = models.ForeignKey(JobPost)
