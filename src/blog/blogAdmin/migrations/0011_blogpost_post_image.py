# Generated by Django 4.2.8 on 2024-01-02 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogAdmin', '0010_alter_blogpost_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='post_image',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]