# Generated by Django 4.2.1 on 2023-10-22 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dos_alamos', '0005_alter_horadisponible_hora_alter_reserva_confirmada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=50)),
            ],
        ),
    ]