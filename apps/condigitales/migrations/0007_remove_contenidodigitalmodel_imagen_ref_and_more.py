# Generated by Django 4.0.5 on 2023-11-24 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0005_alter_competenciamodel_nombre_and_more'),
        ('condigitales', '0006_alter_contenidodigitalmodel_fecha_creacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contenidodigitalmodel',
            name='imagen_ref',
        ),
        migrations.AddField(
            model_name='contenidodigitalmodel',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='contenidos/', verbose_name='Archivo'),
        ),
        migrations.RemoveField(
            model_name='contenidodigitalmodel',
            name='id_poblacion',
        ),
        migrations.AddField(
            model_name='contenidodigitalmodel',
            name='id_poblacion',
            field=models.ManyToManyField(help_text='Id población', related_name='contenidos', to='shared.poblacionmodel', verbose_name='Id población'),
        ),
        migrations.AlterField(
            model_name='contenidodigitalmodel',
            name='url',
            field=models.CharField(help_text='Ingresa la url del contenido', max_length=50, null=True, verbose_name='Url contenido'),
        ),
    ]