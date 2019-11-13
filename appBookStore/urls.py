from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('libros/', views.listaLibros, name='listaLibros'),
    path('autores/', views.listaAutores, name='listaAutores'),
    path('editoriales/', views.listaEditoriales, name='listaEditoriales'),
    path('libros/<int: libro_id>/', views.listaLibros, name='listaLibros'),
    path('autores/<int: autor_id>/', views.listaAutores, name='listaAutores'),
    path('editoriales/<int: editorial_id>/', views.listaEditoriales, name='listaEditoriales'),
]