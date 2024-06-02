from django.contrib import admin
from client.models import Client, Education, Experience, Skill, ProfessionalSummary
# Register your models here.

admin.site.register(Client)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(ProfessionalSummary)