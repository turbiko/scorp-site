# Generated by Django 5.0.4 on 2024-06-03 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contactpage_big_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactdata',
            name='post_addr2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
