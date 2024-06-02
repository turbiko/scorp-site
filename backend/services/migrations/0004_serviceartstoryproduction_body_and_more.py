# Generated by Django 5.0.4 on 2024-06-02 15:24

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_alter_serviceproduction_service_painting'),
        ('wagtailimages', '0026_delete_uploadedimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceartstoryproduction',
            name='body',
            field=wagtail.fields.RichTextField(blank=True, null=True, verbose_name='Body'),
        ),
        migrations.AddField(
            model_name='servicepostproduction',
            name='body',
            field=wagtail.fields.RichTextField(blank=True, null=True, verbose_name='Body'),
        ),
        migrations.AddField(
            model_name='servicepreproduction',
            name='body',
            field=wagtail.fields.RichTextField(blank=True, null=True, verbose_name='Body'),
        ),
        migrations.AddField(
            model_name='serviceproduction',
            name='body',
            field=wagtail.fields.RichTextField(blank=True, null=True, verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='serviceartstoryproduction',
            name='service_painting',
            field=models.ForeignKey(blank=True, help_text='service picture', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AlterField(
            model_name='servicepostproduction',
            name='service_painting',
            field=models.ForeignKey(blank=True, help_text='service picture', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AlterField(
            model_name='servicepreproduction',
            name='service_painting',
            field=models.ForeignKey(blank=True, help_text='service picture', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
