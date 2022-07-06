from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Categoria(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Post(models.Model):
    autor = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    titulo= models.CharField(max_length=200)
    resumen = models.CharField(max_length=500)
    contenido = models.TextField()
    imagen = models.CharField(max_length=200)
    fecha = models.DateTimeField(default= timezone.now)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.titulo} por {self.autor}"

    class Meta:
        ordering = ["-fecha"]


class Comentario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    comentario = models.TextField()
    fecha = models.DateTimeField(default= timezone.now)
    post = models.ForeignKey(Post, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.nombre}, {self.email}"

    class Meta:
        ordering = ["-fecha"]
