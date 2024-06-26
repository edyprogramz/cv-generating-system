# Generated by Django 5.0.6 on 2024-06-07 03:07

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_deploy', models.BooleanField(default=False)),
                ('template_name', models.CharField(max_length=255)),
                ('template_thumbnail', models.ImageField(upload_to='thumbnails/')),
                ('template_file', models.FileField(upload_to='resumes/')),
                ('description', ckeditor.fields.RichTextField(default='Who should use this?')),
                ('categories', models.ManyToManyField(related_name='templates', to='resumes.templatecategory')),
            ],
        ),
    ]
