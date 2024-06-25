# Generated by Django 5.0.4 on 2024-06-25 16:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_career_big_picture'),
        ('wagtailcore', '0093_uploadedfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='redirect_page',
            field=models.ForeignKey(blank=True, help_text='Select a page to redirect to', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page'),
        ),
    ]
