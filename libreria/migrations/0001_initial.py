# Generated by Django 4.1 on 2024-04-24 17:33

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Libro",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("titulo", models.CharField(max_length=100, verbose_name="Título")),
                (
                    "imagen",
                    models.ImageField(
                        null=True, upload_to="imagenes/", verbose_name="Imagen"
                    ),
                ),
                (
                    "description",
                    models.TextField(null=True, verbose_name="Descripción"),
                ),
            ],
        ),
    ]
