# Generated by Django 4.1.5 on 2023-03-11 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0003_remove_proyectosmodel_id_users'),
        ('phases', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phase',
            name='id_phase',
        ),
        migrations.AddField(
            model_name='phase',
            name='id_proyecto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='proyectos.proyectosmodel'),
        ),
    ]