from django.urls import path
from resumes.views import resumes

app_name = 'resumes'

urlpatterns = [
    path('', resumes, name='index'),
] 