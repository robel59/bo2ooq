# Generated by Django 4.2.4 on 2024-07-02 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('htmlemail', '0002_emailtemplate_created_at_emailtemplate_sent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='height',
        ),
        migrations.RemoveField(
            model_name='image',
            name='width',
        ),
    ]
