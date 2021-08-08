from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.

class Portfolio(models.Model):
    img = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=20, null=True, blank=True)
    website_link = models.URLField(null=True, blank=True)
    github_link = models.URLField(null=True, blank=True)
    tag1 = models.CharField(max_length=15, null=True, blank=True)
    tag2 = models.CharField(max_length=15, null=True, blank=True)
    tag3 = models.CharField(max_length=15, null=True, blank=True)
    tag4 = models.CharField(max_length=15, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.title

class TeckStack(models.Model):
    img = models.FileField(null=True,upload_to="techstack/", validators=[FileExtensionValidator(['jpeg', 'png', 'svg'])])
    tech_title = models.CharField(max_length=15, blank=True)
    len_stack = models.IntegerField(null=False)

    class Meta:
        ordering = ['-len_stack']

    def __str__(self):
        return self.tech_title

    
