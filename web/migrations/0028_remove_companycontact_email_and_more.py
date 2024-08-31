# Generated by Django 4.2.4 on 2024-06-18 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0027_apptoken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companycontact',
            name='email',
        ),
        migrations.RemoveField(
            model_name='companycontact',
            name='website',
        ),
        migrations.AddField(
            model_name='companycontact',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='services/'),
        ),
    ]
