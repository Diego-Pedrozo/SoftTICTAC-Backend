# Generated by Django 4.0.5 on 2023-12-11 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectoaula', '0002_alter_actividadmodel_id_proyectoaula'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ActividadModel',
            new_name='ActividadProyectoModel',
        ),
    ]
