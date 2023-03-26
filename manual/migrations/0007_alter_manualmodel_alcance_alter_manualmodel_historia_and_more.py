# Generated by Django 4.1.5 on 2023-03-25 07:55

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manual', '0006_rename_id_proyecto_manualmodel_proyecto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manualmodel',
            name='alcance',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='manualmodel',
            name='historia',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='manualmodel',
            name='mision',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='manualmodel',
            name='politicas',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=150), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='manualmodel',
            name='vision',
            field=models.CharField(max_length=300, null=True),
        ),
    ]