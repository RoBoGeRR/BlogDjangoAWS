# Generated by Django 5.0.7 on 2024-08-09 12:45

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_slug'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('formated', django.db.models.manager.Manager()),
            ],
        ),
    ]
