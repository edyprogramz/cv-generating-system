# Generated by Django 5.0.6 on 2024-05-18 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='about_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='template',
            name='course_pursued',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='template',
            name='email',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='template',
            name='full_name',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='template',
            name='languages',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='template',
            name='location',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='template',
            name='phone_number',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='template',
            name='profile_picture',
            field=models.BooleanField(default=False),
        ),
    ]
