# Generated by Django 3.2.22 on 2024-01-11 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
    ]
