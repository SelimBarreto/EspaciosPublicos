# Generated by Django 5.1.1 on 2024-09-16 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('espacios', '0003_remove_espaciopublico_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='espaciopublico',
            name='delegacion',
            field=models.CharField(max_length=100),
        ),
    ]
