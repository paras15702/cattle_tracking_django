# Generated by Django 4.1 on 2023-02-05 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0006_farmer_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmer',
            name='user',
        ),
    ]