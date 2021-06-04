from django.db import models
from martor.models import MartorField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='project/images/')
    url = models.URLField(blank=True)
    date = models.DateField()

    martorfield = MartorField(blank=True, null=True)

    def __str__(self):
        return self.title
