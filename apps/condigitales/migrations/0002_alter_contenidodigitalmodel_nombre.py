# Generated by Django 4.0.5 on 2023-11-14 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condigitales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenidodigitalmodel',
            name='nombre',
            field=models.CharField(help_text='Ingresa el nombre del contenido', max_length=50, verbose_name='Nombre contenido'),
        ),
    ]
