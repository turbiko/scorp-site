# Generated by Django 5.0.4 on 2024-06-04 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ournews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='article_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
