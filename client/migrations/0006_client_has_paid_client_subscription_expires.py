# Generated by Django 5.0.6 on 2024-06-06 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_alter_client_linkedin_url_alter_client_phone_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='has_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='client',
            name='subscription_expires',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]