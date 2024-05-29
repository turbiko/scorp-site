# Generated by Django 5.0.4 on 2024-05-30 00:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_homepage_about_background_homepage_about_text_and_more'),
        ('wagtailimages', '0026_delete_uploadedimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='partners_background',
            field=models.ForeignKey(blank=True, help_text='Intro top image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
