# Generated by Django 4.2.8 on 2023-12-26 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogAdmin', '0004_alter_blogpost_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]