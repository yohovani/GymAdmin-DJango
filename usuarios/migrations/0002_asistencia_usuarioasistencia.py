# Generated by Django 4.0.1 on 2022-01-21 22:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_asistencia', models.DateTimeField(default=datetime.datetime(2022, 1, 21, 16, 24, 30, 506068))),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioAsistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asistencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asistencia', to='usuarios.asistencia')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to='usuarios.usuario')),
            ],
        ),
    ]
