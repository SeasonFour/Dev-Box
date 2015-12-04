from django.db import models

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=30)
    class Meta:
        verbose_name = "name"
        verbose_name_plural = "names"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Developer(models.Model):
    first_name = models.CharField(max_length=50,blank=False)
    last_name = models.CharField(max_length=50,blank=False)
    email_address = models.EmailField(max_length=50,blank=False)
    bio = models.TextField(max_length=500)
    profile_picture = models.ImageField(blank=True)
    website_url = models.URLField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    languages = models.ManyToManyField(Language,blank=True)

    def __str__(self):
        return "{}'{} {}".format(self.first_name,'s','Details')


class Portfolio(models.Model):
    title = models.CharField(max_length=50,blank=False)
    image = models.ImageField()
    description = models.TextField()
    github_link = models.URLField()
    owner = models.ForeignKey(Developer)

    def __str__(self):
        return self.title