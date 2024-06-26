# Generated by Django 5.0.6 on 2024-06-02 12:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_experience_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='fluency_in_skill',
            field=models.IntegerField(default=10),
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('in_which_company', models.CharField(default='', max_length=100)),
                ('phone_number', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(default='', max_length=100)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
        ),
    ]
