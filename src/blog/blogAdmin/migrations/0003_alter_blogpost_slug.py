# Generated by Django 4.2.8 on 2023-12-25 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogAdmin', '0002_blogpost_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(),
        ),
    ]
