# Generated by Django 5.0.6 on 2024-06-18 23:19

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_postattachment'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('post_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]