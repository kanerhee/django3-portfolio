from django.db import models
from markdownx.models import MarkdownxField
from ckeditor.fields import RichTextField
from martor.models import MartorField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField()
    
    martorfield = MartorField(blank=True, null=True)
    # rtfield = RichTextField(blank=True, null=True)
    # mdfield = MarkdownxField(blank=True, null=True)

    def __str__(self):
        return self.title
