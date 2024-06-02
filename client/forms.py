from django import forms
from client.models import Client, Education, Experience, Skill, ProfessionalSummary, Hobby, Language, Reference
# from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ("profile_img", "first_name", "last_name", "desired_job_title", "phone_number", "country", "city", "linkedIn_url", "email")

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ("institution_name", "institution_location", "program_pursued", "field_of_study", "graduated", "graduation_month", "graduation_year")

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ("job_title", "company", "country", "state", "city", "start_month", "start_year", "end_month","end_year", "description")       

        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ("name", "fluency_in_skill")

class HobbyForm(forms.ModelForm):
    class Meta:
        model = Hobby
        fields = ("name",)

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ("name",)

class ProfessionalSummaryForm(forms.ModelForm):
    class Meta:
        model = ProfessionalSummary
        fields = ("professional_summary",)

    widgets = {
        'professional_summary': forms.Textarea(attrs={'rows': 10}),
    }

class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = ("name","in_which_company","phone_number","email")