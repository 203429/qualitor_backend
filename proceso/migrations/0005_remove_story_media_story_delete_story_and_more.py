# Generated by Django 4.1.5 on 2023-02-06 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proceso', '0004_proceso_media_tipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story_media',
            name='story',
        ),
        migrations.DeleteModel(
            name='Story',
        ),
        migrations.DeleteModel(
            name='Story_Media',
        ),
    ]