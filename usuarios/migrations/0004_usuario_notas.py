# Generated by Django 4.0.1 on 2022-02-28 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_alter_usuario_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='notas',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]