# Generated by Django 4.0.1 on 2022-01-21 23:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0003_alter_tipopago_fecha_pago'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipopago',
            name='fecha_pago',
        ),
        migrations.AddField(
            model_name='pago',
            name='fecha_pago',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 21, 17, 28, 30, 290713)),
        ),
    ]