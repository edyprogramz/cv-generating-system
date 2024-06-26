# Generated by Django 5.0.6 on 2024-06-02 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0005_template_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='num_educations',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='template',
            name='num_experiences',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='template',
            name='num_hobbies',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='template',
            name='num_languages',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='template',
            name='num_references',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='template',
            name='num_skills',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='template',
            name='template_deploy',
            field=models.BooleanField(default=False),
        ),
    ]
