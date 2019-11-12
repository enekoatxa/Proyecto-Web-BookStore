from django.db import models

class Libro(models.Model):
   # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
  # cod_libro = models.IntegerField()
   titulo = models.CharField(max_length=50)
   num_paginas = models.IntegerField()
   genero = models.CharField(max_length=50)
  # portada = models.Imagefield()
   anyo = models.IntegerField()
   edicion = models.IntegerField()
   idioma = models.CharField(max_length=50)
   cod_editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)

class Autor(models.Model):
   # Campo para la relación one-to-many
  # departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
   nombre = models.CharField(max_length=40)
   apellido = models.CharField(max_length=40)
   fecha_nacimiento = models.DateField()
  # foto = models.Imagefield()

class Editorial(models.Model):
   # Campo para la relación one-to-many
  # cod_editorial = models.IntegerField()
   nombre = models.CharField(max_length=40)

class Escribe(models.Model):
   # Campo para la relación one-to-many
   cod_libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
   cod_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)