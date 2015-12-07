from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

class Developer(models.Model):
    first_name = models.CharField(max_length=50,blank=False)
    last_name = models.CharField(max_length=50,blank=False)
    email_address = models.EmailField(max_length=50,blank=False)
    bio = models.TextField(max_length=500)
    profile_picture = models.ImageField(blank=True)
    website_url = models.URLField(null=True)
    years_exp = models.IntegerField(blank=True,default=1,validators=[MinValueValidator(0),
                                                                     MaxValueValidator(50)])
    software_title = models.CharField(blank=True,default="Back-End",max_length=50)
    languages = models.CharField(max_length=1000,blank=True)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "{}'{} {}".format(self.first_name,'s','Details')


class Portfolio(models.Model):
    title = models.CharField(max_length=50,blank=False)
    image = models.ImageField(blank=True)
    description = models.TextField()
    github_link = models.URLField()
    owner = models.ForeignKey(Developer)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title