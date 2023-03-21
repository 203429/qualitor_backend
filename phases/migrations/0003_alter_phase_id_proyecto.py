# Generated by Django 4.1.5 on 2023-03-11 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0003_remove_proyectosmodel_id_users'),
        ('phases', '0002_remove_phase_id_phase_phase_id_proyecto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phase',
            name='id_proyecto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phases_list', related_query_name='phases_list', to='proyectos.proyectosmodel'),
        ),
    ]