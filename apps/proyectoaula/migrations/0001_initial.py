# Generated by Django 4.0.5 on 2023-12-10 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shared', '0005_alter_competenciamodel_nombre_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProyectoAulaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Asigne un nombre al proyecto de aula', max_length=500, verbose_name='Nombre del proyecto de aula')),
                ('grado', models.CharField(help_text='Asigne un grado al proyecto de aula', max_length=50, verbose_name='Grado')),
                ('fecha_inicio', models.DateField(null=True, verbose_name='Fecha de Inicio')),
                ('fecha_fin', models.DateField(null=True, verbose_name='Fecha de Finalización')),
                ('lecciones_aprendidas', models.CharField(help_text='Asigne las Lecciones Aprendidas', max_length=500, null=True, verbose_name='Lecciones Aprendidas')),
                ('id_linea', models.ForeignKey(help_text='Id linea', on_delete=django.db.models.deletion.DO_NOTHING, to='shared.lineatransversalmodel', verbose_name='Id linea')),
                ('user', models.ForeignKey(help_text='Seleccione Usuario', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Proyecto de aula',
                'verbose_name_plural': 'Proyectos de aula',
            },
        ),
        migrations.CreateModel(
            name='ActividadModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Asigne un nombre al proyecto de aula', max_length=500, verbose_name='Nombre del proyecto de aula')),
                ('descripcion', models.CharField(help_text='Asigne una descripción', max_length=50, verbose_name='Descripción')),
                ('estudiantes', models.CharField(help_text='Asigne estudiantes de apoyo', max_length=500, verbose_name='Estudiantes de apoyo')),
                ('cumplimiento', models.BooleanField(default=False, help_text='Cumplimiento', verbose_name='Cumplimiento')),
                ('observaciones', models.CharField(help_text='Asigne Observaciones', max_length=500, null=True, verbose_name='Observaciones')),
                ('fecha_inicio', models.DateField(null=True, verbose_name='Fecha de Inicio')),
                ('fecha_fin', models.DateField(null=True, verbose_name='Fecha de Finalización')),
                ('id_proyectoaula', models.ForeignKey(help_text='Id proyecto aula', on_delete=django.db.models.deletion.CASCADE, to='proyectoaula.proyectoaulamodel', verbose_name='Id proyecto aula')),
            ],
            options={
                'verbose_name': 'Actividad Proyecto de aula',
                'verbose_name_plural': 'Actividades Proyecto de aula',
            },
        ),
    ]
