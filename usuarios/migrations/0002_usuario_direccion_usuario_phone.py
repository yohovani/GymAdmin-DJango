# Generated by Django 4.0.1 on 2022-02-13 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='usuario',
            name='phone',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
