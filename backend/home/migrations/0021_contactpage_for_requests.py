# Generated by Django 5.0.4 on 2024-10-24 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_careertitles_name_en_careertitles_name_uk'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='for_requests',
            field=models.CharField(default='for requests', max_length=255, verbose_name='for requests'),
        ),
    ]
