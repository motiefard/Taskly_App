# Generated by Django 5.1.2 on 2024-12-24 13:04

import task.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_rename_creared_on_task_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='data',
            field=models.FileField(upload_to=task.models.GenerateAttachmentFilePath()),
        ),
    ]
