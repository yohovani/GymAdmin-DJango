# Generated by Django 4.0.1 on 2022-02-28 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caja', '0001_initial'),
        ('orders', '0002_payment_cambio_payment_payment_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cierre_caja',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='caja.cierrecaja'),
        ),
    ]
