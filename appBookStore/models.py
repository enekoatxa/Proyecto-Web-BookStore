from django.db import models


class Autor(models.Model):
   nombre = models.CharField(max_length=40)
   apellido = models.CharField(max_length=40)
   fecha_nacimiento = models.DateField()
   foto = models.ImageField(upload_to='appBookStore/static/img',blank=True,null=True,verbose_name='Image')
   
class Editorial(models.Model):
   nombre = models.CharField(max_length=40)

class Libro(models.Model):
   titulo = models.CharField(max_length=50)
   num_paginas = models.IntegerField()
   genero = models.CharField(max_length=50)
   portada = models.ImageField(upload_to='appBookStore/static/img',blank=True,null=True,verbose_name='Image')
   anyo = models.IntegerField()
   edicion = models.IntegerField()
   idioma = models.CharField(max_length=50)
   cod_editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
   autores = models.ManyToManyField(Autor)