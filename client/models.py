from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, URLValidator
# Create your models here.

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_img = models.ImageField(upload_to='client/profileImg/', null=True, blank=True)
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    phone_number = models.CharField(
        max_length=15,
        null=True, blank=True,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]
    )
    country = models.CharField(max_length=15, default='')
    city = models.CharField(max_length=50, null=True, blank=True)
    linkedIn_url = models.URLField(max_length=500, null=True, blank=True, validators=[URLValidator()])
    desired_job_title = models.CharField(max_length=100, default='')
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.user.username
      
class Experience(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    job_title = models.CharField(max_length=100, default='')
    company = models.CharField(max_length=100, default='')
    country = models.CharField(max_length=15, default='')
    state = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, default='')
    start_month = models.CharField(max_length=100, null=True, blank=True)
    start_year = models.CharField(max_length=100, null=True, blank=True)
    end_month = models.CharField(max_length=100, null=True, blank=True)
    end_year = models.CharField(max_length=100, null=True, blank=True)

    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.job_title} at {self.company}"

class Education(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    institution_name = models.CharField(max_length=100, default='')
    institution_location = models.CharField(max_length=100, default='')
    program_pursued = models.CharField(max_length=100, default='')
    field_of_study = models.CharField(max_length=100, default='')
    graduated = models.BooleanField(default=True)
    graduation_month = models.CharField(max_length=100, null=True, blank=True)
    graduation_year = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.institution_name

class Skill(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    name = models.CharField(max_length=100, default='')
    fluency_in_skill = models.IntegerField(default=10)

    def __str__(self):
        return self.name

class ProfessionalSummary(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)

    professional_summary = models.TextField()

    def __str__(self):
        return self.client.user.username

class Language(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    name = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name
    
class Hobby(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    name = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name
    
class Reference(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    name = models.CharField(max_length=100, default='')
    in_which_company = models.CharField(max_length=100, default='')
    phone_number = models.CharField(
        max_length=15, default='',
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]
    )
    email = models.EmailField(max_length=100, default='')

    def __str__(self):
        return self.name

class Certification(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    name = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name