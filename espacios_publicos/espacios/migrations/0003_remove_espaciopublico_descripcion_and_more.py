# Generated by Django 5.1.1 on 2024-09-16 22:33

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('espacios', '0002_instalaciondeportiva'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='espaciopublico',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='espaciopublico',
            name='responsable',
        ),
        migrations.AddField(
            model_name='espaciopublico',
            name='delegacion',
            field=models.CharField(default='Sin delegacion', max_length=100),
        ),
        migrations.AddField(
            model_name='espaciopublico',
            name='direccion',
            field=models.CharField(default='Sin dirección', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='espaciopublico',
            name='tipo',
            field=models.CharField(default='sin direccion', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='espaciopublico',
            name='nombre',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='espaciopublico',
            name='ubicacion',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326),
        ),
    ]
