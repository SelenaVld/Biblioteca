# Generated by Django 4.1 on 2024-06-06 00:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("libreria", "0002_rename_description_libro_descripcion"),
    ]

    operations = [
        migrations.CreateModel(
            name="Genero",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name="libro",
            name="generos",
            field=models.ManyToManyField(blank=True, to="libreria.genero"),
        ),
    ]
