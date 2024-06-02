from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class TemplateCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Template(models.Model):
    template_deploy = models.BooleanField(default=False)

    template_name = models.CharField(max_length=255)
    template_thumbnail = models.ImageField(upload_to='thumbnails/')
    template_file = models.FileField(upload_to='resumes/')
    categories = models.ManyToManyField(TemplateCategory, related_name='templates')
    description = RichTextField(
        default='Who should use this? | Format and styling details: | MAJOR FEATURES, TEXT DETAILS ...'
    )
    num_educations = models.IntegerField(default=0)
    num_experiences = models.IntegerField(default=0)
    num_skills = models.IntegerField(default=0)
    num_languages = models.IntegerField(default=0)
    num_hobbies = models.IntegerField(default=0)
    num_references = models.IntegerField(default=0)

    
    def __str__(self):
        return self.template_name
