# Generated by Django 5.0.4 on 2024-06-04 10:09

import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ournews', '0002_newsarticle_article_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='article_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='big_text',
            field=wagtail.fields.RichTextField(max_length=62000),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='short_text',
            field=models.TextField(max_length=6500),
        ),
    ]
