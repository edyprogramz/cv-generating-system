# Generated by Django 5.0.6 on 2024-05-20 12:01

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=100)),
                ('institution_location', models.CharField(max_length=100)),
                ('program_pursued', models.CharField(max_length=100)),
                ('field_of_study', models.CharField(max_length=100)),
                ('graduated', models.BooleanField(default=True)),
                ('graduation_month', models.CharField(max_length=100)),
                ('graduation_year', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('start_month', models.CharField(max_length=100)),
                ('start_year', models.CharField(max_length=100)),
                ('end_month', models.CharField(max_length=100)),
                ('end_year', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_img', models.ImageField(upload_to='user/profileImg/')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('LinkedIn', models.CharField(max_length=200)),
                ('proffessional_summary', ckeditor.fields.RichTextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_educations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.education')),
                ('user_experiences', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.experience')),
                ('user_skills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.skills')),
            ],
        ),
    ]