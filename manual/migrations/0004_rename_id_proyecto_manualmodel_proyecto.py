# Generated by Django 4.1.5 on 2023-02-25 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manual', '0003_manualmodel_id_proyecto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manualmodel',
            old_name='id_proyecto',
            new_name='proyecto',
        ),
    ]
