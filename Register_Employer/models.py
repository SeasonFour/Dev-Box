from django.db import models
from shared.DevBoxUser import DevBoxUser,DevBoxCreatedAt
# Create your models here.
class Employer(DevBoxUser):
    company_name = models.CharField(max_length=50,blank=False)
    location = models.CharField(max_length=50,blank=False)

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
