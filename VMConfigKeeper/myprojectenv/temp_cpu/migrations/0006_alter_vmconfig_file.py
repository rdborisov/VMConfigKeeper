# Generated by Django 4.2.11 on 2024-04-11 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temp_cpu', '0005_alter_vmconfig_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vmconfig',
            name='file',
            field=models.FileField(null=True, upload_to='uploads_model'),
        ),
    ]
