# Generated by Django 4.0.5 on 2023-11-15 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0002_alter_lineatransversalmodel_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoblacionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Asigne un nombre a la población', max_length=30, verbose_name='Nombre de población')),
            ],
            options={
                'verbose_name': 'Población',
                'verbose_name_plural': 'Poblaciones',
            },
        ),
    ]
