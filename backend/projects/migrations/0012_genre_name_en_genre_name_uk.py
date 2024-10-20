# Generated by Django 5.0.4 on 2024-10-18 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_project_genres'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='name_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='genre',
            name='name_uk',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
