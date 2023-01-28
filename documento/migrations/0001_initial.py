# Generated by Django 4.1.5 on 2023-01-28 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proceso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('url', models.TextField(default='')),
                ('tipo', models.CharField(max_length=50)),
                ('proceso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documentos', to='proceso.procesomodel')),
            ],
        ),
    ]
