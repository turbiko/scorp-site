# Generated by Django 5.0.4 on 2024-06-08 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_newslist_posts_per_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
