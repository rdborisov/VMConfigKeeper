# Generated by Django 4.2.11 on 2024-04-09 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temp_cpu', '0002_vmconfig_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vmconfig',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
