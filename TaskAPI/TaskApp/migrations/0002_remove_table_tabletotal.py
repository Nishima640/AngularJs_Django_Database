# Generated by Django 5.0.1 on 2024-01-17 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TaskApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='TableTotal',
        ),
    ]
