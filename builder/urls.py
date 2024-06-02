from django.urls import path
from builder.views import index
from builder.views import generate_pdf, generate_docx, resumes, category_resumes

app_name = "builder"

urlpatterns = [
    path('', index, name="home"),
    path('resumes/', resumes, name="browse_resume"),
    path('category-resumes/', category_resumes, name="browse_resume_category"),
    path('generate-pdf/<int:client_id>/<int:template_id>/', generate_pdf, name='generate_pdf'),
    path('generate-docx/<int:client_id>/<int:template_id>/', generate_docx, name='generate_docx'),
]
