# Generated by Django 5.0.4 on 2024-10-07 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_homepage_button_get_in_touch_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='button_skip_intro_link',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='homepage',
            name='button_skip_intro_title',
            field=models.CharField(default='skip intro', max_length=255, verbose_name='skip intro'),
        ),
    ]
