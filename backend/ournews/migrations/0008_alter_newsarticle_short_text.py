# Generated by Django 5.0.4 on 2024-06-04 10:33

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ournews', '0007_newsarticle_news_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='short_text',
            field=wagtail.fields.RichTextField(blank=True, max_length=6500),
        ),
    ]
