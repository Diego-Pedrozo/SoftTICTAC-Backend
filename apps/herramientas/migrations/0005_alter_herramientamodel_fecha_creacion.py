# Generated by Django 4.0.5 on 2023-11-23 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herramientas', '0004_alter_herramientamodel_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='herramientamodel',
            name='fecha_creacion',
            field=models.DateTimeField(default=None, null=True, verbose_name='Fecha de Creacion'),
        ),
    ]
