# Generated by Django 4.0.5 on 2023-11-14 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_userinformationmodel_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformationmodel',
            name='user_type',
            field=models.CharField(choices=[('1', 'Administrativo'), ('2', 'Lider PPT'), ('3', 'Docente')], help_text='Seleccione un tipo de usuario', max_length=255, verbose_name='Tipo de usuario'),
        ),
    ]