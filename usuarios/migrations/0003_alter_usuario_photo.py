# Generated by Django 4.0.1 on 2022-02-13 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuario_direccion_usuario_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
