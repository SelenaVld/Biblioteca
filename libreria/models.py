from django.db import models
from django.contrib.auth.models import User

class Genero(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

# models.py
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name="Título")
    imagen = models.ImageField(upload_to="imagenes/", verbose_name="Imagen", null=True, blank=True)
    descripcion = models.TextField(verbose_name="Descripción", null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")
    pdf = models.FileField(upload_to='pdfs/', null=True, blank=True, verbose_name="Archivo PDF")  # Nuevo campo

    def __str__(self):
        return self.titulo

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        if self.pdf:
            self.pdf.storage.delete(self.pdf.name)
        super().delete()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favoritos = models.ManyToManyField(Libro, blank=True)
    imagen = models.ImageField(upload_to='profile_images/', null=True, blank=True)  # Añadido

    def __str__(self):
        return self.user.username
