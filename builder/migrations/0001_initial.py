# Generated by Django 5.0.6 on 2024-05-18 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_name', models.CharField(max_length=255)),
                ('template_thumbnail', models.ImageField(upload_to='thumbnails/')),
                ('template_file', models.FileField(upload_to='templates/')),
            ],
        ),
    ]
