# Generated by Django 5.0.4 on 2024-10-20 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_contactdata_email_en_contactdata_email_requests_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='for_requests',
            field=models.CharField(default='for requests', max_length=255, verbose_name='for requests'),
        ),
    ]
