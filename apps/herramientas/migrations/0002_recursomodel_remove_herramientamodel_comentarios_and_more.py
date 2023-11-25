# Generated by Django 4.0.5 on 2023-11-23 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herramientas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecursoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('1', 'Video'), ('2', 'Imagen'), ('3', 'Proyector'), ('4', 'Sonido'), ('5', 'Computador')], help_text='Seleccione un tipo de recurso', max_length=100, verbose_name='Tipo de recurso')),
            ],
            options={
                'verbose_name': 'Recurso',
                'verbose_name_plural': 'Recursos',
            },
        ),
        migrations.RemoveField(
            model_name='herramientamodel',
            name='comentarios',
        ),
        migrations.AddField(
            model_name='herramientamodel',
            name='revision',
            field=models.CharField(default='Sin revisión', help_text='Asigne una revisión', max_length=500, null=True, verbose_name='Revisión'),
        ),
        migrations.AlterField(
            model_name='herramientamodel',
            name='recomendacion',
            field=models.CharField(help_text='Asigne una Recomendación', max_length=500, null=True, verbose_name='Recomendación'),
        ),
        migrations.CreateModel(
            name='ProcesoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Asigne un nombre al proceso', max_length=30, verbose_name='Nombre del proceso')),
                ('descripcion', models.CharField(default='Sin descripción', help_text='Ingresa la descripción del proceso', max_length=500, verbose_name='Descripción proceso')),
                ('tiempo', models.IntegerField(help_text='Ingresa el tiempo del proceso', verbose_name='Tiempo del proceso')),
                ('recurso', models.ManyToManyField(help_text='Id recurso', related_name='procesos', to='herramientas.recursomodel', verbose_name='Id recurso')),
            ],
            options={
                'verbose_name': 'Proceso',
                'verbose_name_plural': 'Procesos',
            },
        ),
        migrations.CreateModel(
            name='MomentoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Asigne un nombre al momento', max_length=30, verbose_name='Nombre del momento')),
                ('descripcion', models.CharField(default='Sin descripción', help_text='Ingresa la descripción del momento', max_length=500, verbose_name='Descripción momento')),
                ('proceso', models.ManyToManyField(help_text='Id proceso', related_name='momentos', to='herramientas.procesomodel', verbose_name='Id proceso')),
            ],
            options={
                'verbose_name': 'Momento',
                'verbose_name_plural': 'Momentos',
            },
        ),
        migrations.AddField(
            model_name='herramientamodel',
            name='momento',
            field=models.ManyToManyField(help_text='Id momentos', related_name='herramientas', to='herramientas.momentomodel', verbose_name='Id Momento'),
        ),
    ]