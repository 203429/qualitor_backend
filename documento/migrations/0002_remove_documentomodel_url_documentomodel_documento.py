# Generated by Django 4.1.5 on 2023-01-28 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documento', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentomodel',
            name='url',
        ),
        migrations.AddField(
            model_name='documentomodel',
            name='documento',
            field=models.ImageField(blank=True, null=True, upload_to='resources'),
        ),
    ]
