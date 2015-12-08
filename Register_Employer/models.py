from django.db import models
from shared.DevBoxUser import DevBoxUser
# Create your models here.
class Employer(DevBoxUser):
    company_name = models.CharField(max_length=50,blank=False)
