# Generated by Django 4.0.5 on 2023-11-23 22:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('herramientas', '0002_recursomodel_remove_herramientamodel_comentarios_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='herramientamodel',
            old_name='objetivos',
            new_name='objetivo',
        ),
        migrations.RemoveField(
            model_name='herramientamodel',
            name='momento',
        ),
        migrations.RemoveField(
            model_name='momentomodel',
            name='proceso',
        ),
        migrations.RemoveField(
            model_name='procesomodel',
            name='recurso',
        ),
        # migrations.AddField(
        #     model_name='procesomodel',
        #     name='id_momento',
        #     field=models.ForeignKey(default=1, help_text='Id momento', on_delete=django.db.models.deletion.DO_NOTHING, to='herramientas.momentomodel', verbose_name='Id momento'),
        #     preserve_default=False,
        # ),
        # migrations.AddField(
        #     model_name='recursomodel',
        #     name='id_proceso',
        #     field=models.ForeignKey(default=1, help_text='Id proceso', on_delete=django.db.models.deletion.DO_NOTHING, to='herramientas.procesomodel', verbose_name='Id proceso'),
        #     preserve_default=False,
        # ),
    ]