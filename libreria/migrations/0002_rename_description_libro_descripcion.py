# Generated by Django 4.1 on 2024-04-24 20:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("libreria", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="libro",
            old_name="description",
            new_name="descripcion",
        ),
    ]
