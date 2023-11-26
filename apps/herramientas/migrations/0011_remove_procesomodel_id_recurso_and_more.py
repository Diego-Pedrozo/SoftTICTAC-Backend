# Generated by Django 4.0.5 on 2023-11-25 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0005_alter_competenciamodel_nombre_and_more'),
        ('herramientas', '0010_procesomodel_id_recurso_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='procesomodel',
            name='id_recurso',
        ),
        migrations.RemoveField(
            model_name='procesomodel',
            name='nombre',
        ),
        migrations.AddField(
            model_name='procesomodel',
            name='recurso',
            field=models.CharField(default='Sin recursos', help_text='Asigne recursos', max_length=500, null=True, verbose_name='Recursos'),
        ),
        migrations.RemoveField(
            model_name='herramientamodel',
            name='id_poblacion',
        ),
        migrations.AddField(
            model_name='herramientamodel',
            name='id_poblacion',
            field=models.ManyToManyField(help_text='Id población', related_name='herramientas', to='shared.poblacionmodel', verbose_name='Id población'),
        ),
        migrations.AlterField(
            model_name='momentomodel',
            name='id_herramienta',
            field=models.ForeignKey(help_text='Id herramienta', on_delete=django.db.models.deletion.CASCADE, related_name='momentos', to='herramientas.herramientamodel', verbose_name='Id herramienta'),
        ),
        migrations.AlterField(
            model_name='procesomodel',
            name='id_momento',
            field=models.ForeignKey(help_text='Id momento', on_delete=django.db.models.deletion.CASCADE, related_name='procesos', to='herramientas.momentomodel', verbose_name='Id momento'),
        ),
    ]
