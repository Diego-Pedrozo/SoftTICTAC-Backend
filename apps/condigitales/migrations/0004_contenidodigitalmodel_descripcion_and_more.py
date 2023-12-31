# Generated by Django 4.0.5 on 2023-11-15 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0003_poblacionmodel'),
        ('condigitales', '0003_alter_contenidodigitalmodel_visibilidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='contenidodigitalmodel',
            name='descripcion',
            field=models.CharField(default='Sin descripción', help_text='Ingresa la descripción del contenido', max_length=255, verbose_name='Descripción contenido'),
        ),
        migrations.AddField(
            model_name='contenidodigitalmodel',
            name='id_poblacion',
            field=models.ForeignKey(help_text='Id población', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shared.poblacionmodel', verbose_name='Id población'),
        ),
        migrations.AddField(
            model_name='contenidodigitalmodel',
            name='imagen_ref',
            field=models.ImageField(blank=True, null=True, upload_to='contenidos/', verbose_name='Imagen'),
        ),
    ]
