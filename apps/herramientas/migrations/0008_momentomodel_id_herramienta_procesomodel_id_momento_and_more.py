# Generated by Django 4.0.5 on 2023-11-24 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('herramientas', '0007_alter_herramientamodel_fecha_creacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='momentomodel',
            name='id_herramienta',
            field=models.ForeignKey(help_text='Id herramienta', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='herramientas.herramientamodel', verbose_name='Id herramienta'),
        ),
        migrations.AddField(
            model_name='procesomodel',
            name='id_momento',
            field=models.ForeignKey(help_text='Id momento', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='herramientas.momentomodel', verbose_name='Id momento'),
        ),
        migrations.AlterField(
            model_name='herramientamodel',
            name='fecha_creacion',
            field=models.DateTimeField(null=True, verbose_name='Fecha de Creacion'),
        ),
        migrations.AlterField(
            model_name='recursomodel',
            name='tipo',
            field=models.CharField(help_text='Seleccione un tipo de recurso', max_length=100, verbose_name='Tipo de recurso'),
        ),
    ]
