# Generated by Django 4.0.1 on 2022-02-28 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='cambio',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_paid',
            field=models.FloatField(default=0),
        ),
    ]
