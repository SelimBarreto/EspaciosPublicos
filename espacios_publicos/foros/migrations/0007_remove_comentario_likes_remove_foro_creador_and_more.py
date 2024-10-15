# Generated by Django 5.1.1 on 2024-09-17 09:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('espacios', '0004_alter_espaciopublico_delegacion'),
        ('foros', '0006_alter_foro_creador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='foro',
            name='creador',
        ),
        migrations.AlterField(
            model_name='comentario',
            name='foro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='foros.foro'),
        ),
        migrations.AlterField(
            model_name='foro',
            name='espacio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='espacios.instalaciondeportiva'),
        ),
    ]