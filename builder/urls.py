from django.urls import path
from builder.views import generate_pdf, generate_docx, index

app_name = "builder"

urlpatterns = [
    path('', index, name="home"),
    path('generate-pdf/<int:client_id>/<int:template_id>/', generate_pdf, name='generate_pdf'),
    path('generate-docx/<int:client_id>/<int:template_id>/', generate_docx, name='generate_docx'),
]
