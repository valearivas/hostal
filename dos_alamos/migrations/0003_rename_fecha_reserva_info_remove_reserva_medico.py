# Generated by Django 4.0.4 on 2023-05-15 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dos_alamos', '0002_remove_reserva_hora_alter_reserva_fecha'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserva',
            old_name='fecha',
            new_name='info',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='medico',
        ),
    ]
