# Generated by Django 5.0.6 on 2024-05-28 20:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0004_templatecategory_template_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='description',
            field=ckeditor.fields.RichTextField(default='Who should use this? | Format and styling details: | MAJOR FEATURES, TEXT DETAILS ...'),
        ),
    ]