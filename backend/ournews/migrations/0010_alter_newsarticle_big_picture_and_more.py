# Generated by Django 5.0.4 on 2024-06-12 08:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ournews', '0009_newsarticle_news_for_project'),
        ('wagtailimages', '0026_delete_uploadedimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='big_picture',
            field=models.ForeignKey(blank=True, help_text='news top image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='slider_image',
            field=models.ForeignKey(blank=True, help_text='news image for slider 500x359', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]