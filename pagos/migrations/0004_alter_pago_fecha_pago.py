# Generated by Django 4.0.1 on 2022-02-23 22:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0003_alter_pago_fecha_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='fecha_pago',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 23, 22, 57, 24, 209925)),
        ),
    ]
