# Generated by Django 4.0.5 on 2023-11-14 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LineaTransversalModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Asigne un nombre a la linea transversal', max_length=30, verbose_name='Nombre de linea transversal')),
            ],
            options={
                'verbose_name': 'Linea transversal',
                'verbose_name_plural': 'Lineas transversales',
            },
        ),
    ]
