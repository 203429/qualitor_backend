# Generated by Django 4.1.5 on 2023-03-27 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manual', '0007_alter_manualmodel_alcance_alter_manualmodel_historia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manualmodel',
            name='funciones_puestos',
            field=models.FileField(blank=True, null=True, upload_to='proceso_media/'),
        ),
        migrations.AlterField(
            model_name='manualmodel',
            name='organigrama',
            field=models.FileField(blank=True, null=True, upload_to='proceso_media/'),
        ),
        migrations.AlterField(
            model_name='manualmodel',
            name='organizacion_empresa',
            field=models.FileField(blank=True, null=True, upload_to='proceso_media/'),
        ),
        migrations.AlterField(
            model_name='manualmodel',
            name='vocabulario',
            field=models.FileField(blank=True, null=True, upload_to='proceso_media/'),
        ),
    ]
