# Generated by Django 4.0.1 on 2022-02-28 17:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0013_alter_pago_fecha_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='fecha_pago',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 28, 17, 13, 4, 701148)),
        ),
    ]
