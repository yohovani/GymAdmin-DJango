# Generated by Django 4.0.1 on 2022-02-28 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caja', '0001_initial'),
        ('orders', '0006_alter_order_cierre_caja'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cierre_caja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='caja.cierrecaja'),
        ),
    ]
