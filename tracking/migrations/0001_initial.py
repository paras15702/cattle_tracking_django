# Generated by Django 4.1 on 2023-02-04 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cattle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('breed', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('weight', models.PositiveIntegerField()),
                ('location', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]