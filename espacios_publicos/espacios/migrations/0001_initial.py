# Generated by Django 5.1.1 on 2024-09-16 08:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EspacioPublico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('responsable', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.usuario')),
            ],
        ),
    ]
