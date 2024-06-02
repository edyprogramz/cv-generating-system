from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from client.forms import ClientForm, EducationForm, ExperienceForm, SkillForm, ProfessionalSummaryForm, HobbyForm, LanguageForm, ReferenceForm
from client.models import Client, Experience, Education, Skill, ProfessionalSummary, Hobby, Language, Reference

# Create your views here.
def contact(request):
    if request.user.is_authenticated:
        client, created = Client.objects.get_or_create(user=request.user)
    else:
        client = None

    # contact form 
    if request.method == 'POST':
        if request.user.is_authenticated:
            contact_form = ClientForm(request.POST, request.FILES, instance=client)
            if contact_form.is_valid():
                contact_form.save()
                return redirect("client:client_contact_page")
        else:
            return redirect("user:signup")
    else:
        contact_form = ClientForm(instance=client)

    return render(request, "contact.html", {
        "contact_form":contact_form,  
        "active_page": "contact",
    })

@login_required
def experience(request):
    client = get_object_or_404(Client, user=request.user)
    experiences = Experience.objects.filter(client=client)

    if request.method == 'POST':
        experience_form = ExperienceForm(request.POST)
        if experience_form.is_valid():
            experience = experience_form.save(commit=False)
            experience.client = client
            experience.save()
            return redirect("client:client_experience_page")
        
    else:
        experience_form = ExperienceForm()

    return render(request, "experience/index.html", {
        "experiences":experiences,
        "experience_form":experience_form,
        "active_page": "experience",
    })

@login_required
def edit_experience(request, pk):
    experience = get_object_or_404(Experience, pk=pk, client__user=request.user)

    if request.method == 'POST':
        edit_experience_form = ExperienceForm(request.POST, instance=experience)
        if edit_experience_form.is_valid():
            edit_experience_form.save()
            return redirect("client:client_experience_page")
        
    else:
        edit_experience_form = ExperienceForm(instance=experience)

    return render(request, "experience/edit.html", {
        "edit_experience_form":edit_experience_form,
    })

@login_required
def delete_experience(request, pk):
    experience = get_object_or_404(Experience, pk=pk, client__user=request.user)
    if request.method == 'POST':
        experience.delete()
        return redirect('client:client_experience_page')
    return redirect('client:client_experience_page')

@login_required
def education(request):
    client = get_object_or_404(Client, user=request.user)
    educations = Education.objects.filter(client=client)

    if request.method == 'POST':
        education_form = EducationForm(request.POST)
        if education_form.is_valid():
            education = education_form.save(commit=False)
            education.client = client
            education.save()
            return redirect("client:client_education_page")

    else:
        education_form = EducationForm()
    return render(request, "education/index.html", {
        "educations":educations,
        "education_form":education_form,
        "active_page": "education",
    })

@login_required
def edit_education(request, pk):
    education = get_object_or_404(Education, pk=pk, client__user=request.user)

    if request.method == 'POST':
        edit_education_form = EducationForm(request.POST, instance=education)
        if edit_education_form.is_valid():
            edit_education_form.save()
            return redirect("client:client_education_page")
    else:
        edit_education_form = EducationForm(instance=education)
    return render(request, "education/edit.html", {
        "edit_education_form":edit_education_form,
    })

@login_required
def delete_education(request, pk):
    education = get_object_or_404(Education, pk=pk, client__user=request.user)
    if request.method == 'POST':
        education.delete()
        return redirect("client:client_education_page")
    return redirect("client:client_education_page")

@login_required
def skill(request):
    client = get_object_or_404(Client, user=request.user)
    skills = Skill.objects.filter(client=client)

    if request.method == 'POST':
        skill_form = SkillForm(request.POST)
        if skill_form.is_valid():
            skill = skill_form.save(commit=False)
            skill.client = client
            skill.save()
            return redirect("client:client_skill_page")
        
    else:
        skill_form = SkillForm()

    return render(request, "skill/index.html", {
        "skills":skills,
        "skill_form":skill_form,
        "active_page": "skill",
    })

@login_required
def edit_skill(request, pk):
    skill = get_object_or_404(Skill, pk=pk, client__user=request.user)

    if request.method == 'POST':
        edit_skill_form = SkillForm(request.POST, instance=skill)
        if edit_skill_form.is_valid():
            edit_skill_form.save()
            return redirect("client:client_skill_page")
    else:
        edit_skill_form = SkillForm(instance=skill)
    return render(request, "skill/edit.html", {
        "edit_skill_form":edit_skill_form,
    })

@login_required
def delete_skill(request, pk):
    skill = get_object_or_404(Skill, pk=pk, client__user=request.user)
    if request.method == 'POST':
        skill.delete()
        return redirect("client:client_skill_page")
    return redirect("client:client_skill_page")

@login_required
def summary(request):
    client = get_object_or_404(Client, user=request.user)
    try:
        pro_summary = ProfessionalSummary.objects.get(client=client)
    except ProfessionalSummary.DoesNotExist:
        pro_summary = None

    if request.method == 'POST':
        summary_form = ProfessionalSummaryForm(request.POST, instance=pro_summary)
        if summary_form.is_valid():
            summary = summary_form.save(commit=False)
            summary.client = client
            summary.save()
            return redirect("client:client_summary_page")
    else:
        summary_form = ProfessionalSummaryForm(instance=pro_summary)

    return render(request, "summary/index.html", {
        "summary_form": summary_form,
        "active_page": "summary",
    })

@login_required
def hobby(request):
    client = get_object_or_404(Client, user=request.user)
    hobbies = Hobby.objects.filter(client=client)

    if request.method == 'POST':
        hobby_form = HobbyForm(request.POST)
        if hobby_form.is_valid():
            hobby = hobby_form.save(commit=False)
            hobby.client = client
            hobby.save()
            return redirect("client:client_hobby_page")
        
    else:
        hobby_form = HobbyForm()

    return render(request, "hobby/index.html", {
        "hobbies":hobbies,
        "hobby_form":hobby_form,
        "active_page": "hobby",
    })

@login_required
def edit_hobby(request, pk):
    hobby = get_object_or_404(Hobby, pk=pk, client__user=request.user)

    if request.method == 'POST':
        edit_hobby_form = HobbyForm(request.POST, instance=hobby)
        if edit_hobby_form.is_valid():
            edit_hobby_form.save()
            return redirect("client:client_hobby_page")
    else:
        edit_hobby_form = HobbyForm(instance=hobby)
    return render(request, "hobby/edit.html", {
        "edit_hobby_form":edit_hobby_form,
    })

@login_required
def delete_hobby(request, pk):
    hobby = get_object_or_404(Hobby, pk=pk, client__user=request.user)
    if request.method == 'POST':
        hobby.delete()
        return redirect("client:client_hobby_page")
    return redirect("client:client_hobby_page")

@login_required
def language(request):
    client = get_object_or_404(Client, user=request.user)
    languages = Language.objects.filter(client=client)

    if request.method == 'POST':
        language_form = LanguageForm(request.POST)
        if language_form.is_valid():
            language = language_form.save(commit=False)
            language.client = client
            language.save()
            return redirect("client:client_language_page")
        
    else:
        language_form = LanguageForm()

    return render(request, "language/index.html", {
        "languages":languages,
        "language_form":language_form,
        "active_page": "language",
    })

@login_required
def edit_language(request, pk):
    language = get_object_or_404(Language, pk=pk, client__user=request.user)

    if request.method == 'POST':
        edit_language_form = LanguageForm(request.POST, instance=language)
        if edit_language_form.is_valid():
            edit_language_form.save()
            return redirect("client:client_language_page")
    else:
        edit_language_form = LanguageForm(instance=language)
    return render(request, "language/edit.html", {
        "edit_language_form":edit_language_form,
    })

@login_required
def delete_language(request, pk):
    language = get_object_or_404(Language, pk=pk, client__user=request.user)
    if request.method == 'POST':
        language.delete()
        return redirect("client:client_language_page")
    return redirect("client:client_language_page")

@login_required
def reference(request):
    client = get_object_or_404(Client, user=request.user)
    references = Reference.objects.filter(client=client)

    if request.method == 'POST':
        reference_form = ReferenceForm(request.POST)
        if reference_form.is_valid():
            reference = reference_form.save(commit=False)
            reference.client = client
            reference.save()
            return redirect("client:client_reference_page")
        else:
            reference_form = ReferenceForm()

    return render(request, "reference/index.html", {
        "references":references,
        "reference_form":reference_form,
        "active_page":"reference",
    })

@login_required
def edit_reference(request, pk):
    reference = get_object_or_404(Reference, pk=pk, client__user=request.user)

    if request.method == 'POST':
        edit_reference_form = ReferenceForm(request.POST, instance=reference)
        if edit_reference_form.is_valid():
            edit_reference_form.save()
            return redirect("client:client_reference_page")
        else:
            edit_reference_form = ReferenceForm(instance=reference)
    return render(request, "reference/edit.html", {
        "edit_reference_form":edit_reference_form,
    })

@login_required
def delete_reference(request, pk):
    reference = get_object_or_404(Reference, pk=pk, client__user=request.user)
    if request.method == 'POST':
        reference.delete()
        return redirect("client:client_reference_page")
    return redirect("client:client_reference_page")
