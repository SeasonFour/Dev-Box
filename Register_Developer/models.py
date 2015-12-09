from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from shared.DevBoxUser import DevBoxUser
#Create your models here.
"""this is the model that contains details about the developer"""
class Developer(DevBoxUser):
    bio = models.TextField(verbose_name="About You",max_length=500)
    profile_picture = models.ImageField(blank=True)
    website_url = models.URLField(null=True)
    years_exp = models.IntegerField(verbose_name="Years of experience",
                                    blank=True,default=1,
                                    validators=[MinValueValidator(0),
                                               MaxValueValidator(50)])
    software_title = models.CharField(blank=True,default="Back-End",max_length=50)
    languages = models.CharField(verbose_name="Programming Languages",
                                 max_length=1000,blank=True)
    def __str__(self):
        return "{}'{} {}".format(self.first_name,'s','Details')


"""this is the model that contains the developer's portfolio,
    in relation to the developer"""
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