# Generated by Django 4.2.8 on 2024-01-02 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogAdmin', '0008_blogpost_publish_date_blogpost_timestamp_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-publish_date']},
        ),
    ]
