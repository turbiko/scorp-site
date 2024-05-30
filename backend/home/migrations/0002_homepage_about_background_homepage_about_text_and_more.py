# Generated by Django 5.0.4 on 2024-05-29 23:56

import django.db.models.deletion
import modelcluster.fields
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
        ('wagtailcore', '0093_uploadedfile'),
        ('wagtailimages', '0026_delete_uploadedimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='about_background',
            field=models.ForeignKey(blank=True, help_text='Intro top image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='about_text',
            field=wagtail.fields.RichTextField(default=1, verbose_name='About'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block3_background',
            field=models.ForeignKey(blank=True, help_text='Intro top image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='partners_title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Name for partners block'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='projects_title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Name for projects block'),
        ),
        migrations.CreateModel(
            name='PartnersLogotypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('logotype', models.ForeignKey(blank=True, help_text='Partner name, URL and logotype', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='partner_logo', to='wagtailcore.page')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]