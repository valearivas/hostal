# Generated by Django 4.0.4 on 2023-05-15 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dos_alamos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='hora',
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dos_alamos.horadisponible', verbose_name='FECHA'),
        ),
    ]
