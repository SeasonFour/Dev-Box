from django.db import models

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=30)
    class Meta:
        verbose_name = "name"
        verbose_name_plural = "names"
        ordering = ["name"]


class Developer(models.Model):
    first_name = models.CharField(max_length=50,blank=False)
    last_name = models.CharField(max_length=50,blank=False)
    email_address = models.EmailField(max_length=50,blank=False)
    bio = models.TextField()
    profile_picture = models.ImageField()
    languages = models.ManyToManyField(Language,blank=True)

class Portfolio(models.Model):
    title = models.CharField(max_length=50,blank=False)
    image = models.ImageField()
    description = models.TextField()
    github_link = models.URLField()
    owner = models.ForeignKey(Developer)




