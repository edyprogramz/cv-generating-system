from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# from user.models import Client, Education, Experience, Skill, ProfessionalSummary


# myforms
# class ClientForm(forms.ModelForm):
#     class Meta:
#         model = Client
#         fields = ("profile_img", "first_name", "last_name", "desired_job_title", "phone_number", "country", "city", "linkedIn_url", "proffessional_summary", "email")

#         profile_img = forms.ImageField(
#             label="Profile Image",
#             widget=forms.FileInput(attrs={
#                 "placeholder": "Upload Profile Image",
#                 # "class": "input-field"
#             })
#         )
        
#         first_name = forms.CharField(
#             label="First Name",
#             widget=forms.TextInput(attrs={
#                 "placeholder": "",
#                 # "class": "input-field"
#             })
#         )

#         last_name = forms.CharField(
#             label="Last Name",
#             widget=forms.TextInput(attrs={
#                 "placeholder": "",
#                 # "class": "input-field"
#             })
#         )

#         desired_job_title = forms.CharField(
#             label="Desired Job Title",
#             widget=forms.TextInput(attrs={
#                 "placeholder": "",
#                 # "class": "input-field"
#             })
#         )

#         phone_number = forms.CharField(
#             label="Phone Number",
#             widget=forms.TextInput(attrs={
#                 "placeholder": "Enter Phone Number",
#                 # "class": "input-field"
#             })
#         )

#         country = forms.CharField(
#             label="Country",
#             widget=forms.TextInput(attrs={
#                 "placeholder": "Enter Country",
#                 # "class": "input-field"
#             })
#         )

    
#         city = forms.CharField(
#             label="City",
#             widget=forms.TextInput(attrs={
#                 "placeholder": "Enter City",
#                 # "class": "input-field"
#             })
#         )

#         email = forms.EmailField(
#             label="Email",
#             widget=forms.EmailInput(attrs={
#             "placeholder": "",
#             # "class": "input-field"
#             })
#         )

#         linkedIn_url = forms.URLField(
#             label="LinkedIn",
#             widget=forms.URLInput(attrs={
#                 "placeholder": "Enter LinkedIn Profile URL",
#                 # "class": "input-field"
#             })
#         )

#         professional_summary = forms.CharField(
#             label="Professional Summary",
#             widget=forms.Textarea(attrs={
#                 "placeholder": "Enter Professional Summary",
#                 # "class": "input-field"
#             })
#         )

# class EducationForm(forms.ModelForm):
#     class Meta:
#         model = Education
#         fields = ("institution_name", "institution_location", "program_pursued", "field_of_study", "graduated", "graduation_month", "graduation_year")

# class ExperienceForm(forms.ModelForm):
#     class Meta:
#         model = Experience
#         fields = ("job_title", "company", "country", "state", "city", "start_month", "start_year", "end_month","end_year")       


# class SkillForm(forms.ModelForm):
#     class Meta:
#         model = Skill
#         fields = ("name",)

# class ProfessionalSummaryForm(forms.ModelForm):
#     class Meta:
#         model = ProfessionalSummary
#         fields = ("professional_summary",)



class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Email"

    username = forms.EmailField(
        label="email address",
        widget=forms.EmailInput(attrs={
        "placeholder": "",
        # "class": "input-field"
    }))

    password = forms.CharField(
        label="your password",
        widget=forms.PasswordInput(attrs={
        "placeholder": "",
        # "class": "input-field"
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.username = self.cleaned_data['email']  # Set the username to the email
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
        
        
    email = forms.EmailField(
        label="add your email address",
        widget=forms.EmailInput(attrs={
        "placeholder": "",
        # "class": "input-field"
    }))
    password1 = forms.CharField(
        label="create a password",
        widget=forms.PasswordInput(attrs={
        "placeholder": "",
        # "class": "input-field"
    }))
    password2 = forms.CharField(
        label="re-enter password",
        widget=forms.PasswordInput(attrs={
        "placeholder": "",
        # "placeholder": "re-enter the password",
        # "class": "input-field"
    }))