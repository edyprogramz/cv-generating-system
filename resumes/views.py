from django.shortcuts import render, get_object_or_404
from client.models import Client
from resumes.models import Template as TemplateModel, TemplateCategory

# Create your views here.
def resumes(request):
    client = get_object_or_404(Client, user=request.user)
    templates = TemplateModel.objects.all()
    categories = TemplateCategory.objects.all()

    return render(request, "resumes.html", {
        "templates":templates,
        "categories":categories,
        "client": client
    })