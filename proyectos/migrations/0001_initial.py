# Generated by Django 4.1.7 on 2023-02-23 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProyectosModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_proyect', models.CharField(max_length=50)),
                ('id_users', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('manual', models.FileField(blank=True, null=True, upload_to='resources')),
            ],
        ),
    ]