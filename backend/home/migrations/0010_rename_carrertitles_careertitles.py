# Generated by Django 5.0.4 on 2024-06-08 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_careerjoin_action_text'),
        ('wagtailcore', '0093_uploadedfile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CarrerTitles',
            new_name='CareerTitles',
        ),
    ]