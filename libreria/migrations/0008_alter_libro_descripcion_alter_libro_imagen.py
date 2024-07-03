# Generated by Django 4.1 on 2024-06-11 20:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("libreria", "0007_profile_imagen"),
    ]

    operations = [
        migrations.AlterField(
            model_name="libro",
            name="descripcion",
            field=models.TextField(blank=True, null=True, verbose_name="Descripción"),
        ),
        migrations.AlterField(
            model_name="libro",
            name="imagen",
            field=models.ImageField(
                blank=True, null=True, upload_to="imagenes/", verbose_name="Imagen"
            ),
        ),
    ]