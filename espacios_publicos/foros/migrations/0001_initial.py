# Generated by Django 5.1.1 on 2024-09-16 08:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('espacios', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tema', models.CharField(max_length=255)),
                ('contenido', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
                ('espacio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='espacios.espaciopublico')),
            ],
        ),
    ]