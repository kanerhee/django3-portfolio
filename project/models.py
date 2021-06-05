from django.db import models
from martor.models import MartorField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='project/images/')
    url = models.URLField(blank=True)
    date = models.DateField()

    subject = models.TextField(blank=True, null=True)

    martorfield = MartorField(blank=True, null=True)

    def __str__(self):
        return self.title

    # def get_subject(self):
    #     return json.loads(self.subject)
