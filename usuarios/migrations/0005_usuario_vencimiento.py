# Generated by Django 4.0.1 on 2022-03-08 12:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_usuario_notas'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='vencimiento',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
    ]