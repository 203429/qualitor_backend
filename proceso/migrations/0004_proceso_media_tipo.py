# Generated by Django 4.1.5 on 2023-02-06 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proceso', '0003_proceso_proceso_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='proceso_media',
            name='tipo',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
