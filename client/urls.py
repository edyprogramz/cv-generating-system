from django.urls import path
from client.views import contact, experience, edit_experience, education, edit_education, skill, edit_skill, summary, delete_experience, delete_education, delete_skill, hobby, edit_hobby, delete_hobby, language, edit_language, delete_language, reference, edit_reference, delete_reference, certification, edit_certification, delete_certification

app_name = "client" 

urlpatterns = [
    path('', contact, name="client_contact_page"),
    path('experience/', experience, name="client_experience_page"),
    path('experience/<int:pk>/', edit_experience, name="edit_experience"),
    path('experience/<int:pk>/delete/', delete_experience, name="delete_experience"),

    path('education/', education, name="client_education_page"),
    path('education/<int:pk>/', edit_education, name="edit_education"),
    path('education/<int:pk>/delete/', delete_education, name="delete_education"),

    path('skill', skill, name="client_skill_page"),
    path('skill/<int:pk>/', edit_skill, name="edit_skill"),
    path('skill/<int:pk>/delete/', delete_skill, name="delete_skill"),

    path('hobby/', hobby, name="client_hobby_page"),
    path('hobby/<int:pk>/', edit_hobby, name="edit_hobby"),
    path('hobby/<int:pk>/delete/', delete_hobby, name="delete_hobby"),

    path('language/', language, name="client_language_page"),
    path('language/<int:pk>/', edit_language, name="edit_language"),
    path('language/<int:pk>/delete/', delete_language, name="delete_language"),

    path('reference/', reference, name="client_reference_page"),
    path('reference/<int:pk>/', edit_reference, name="edit_reference"),
    path('reference/<int:pk>/delete/', delete_reference, name="delete_reference"),

    path('certification/', certification, name="client_certification_page"),
    path('certification/<int:pk>/', edit_certification, name="edit_certification"),
    path('certification/<int:pk>/delete/', delete_certification, name="delete_certification"),

    path('summary/', summary, name="client_summary_page"),
]