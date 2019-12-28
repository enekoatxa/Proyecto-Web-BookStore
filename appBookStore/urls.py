from django.urls import path
from . import views

urlpatterns = [
	path('ajax/<int:libro_id>/', views.ajax, name='ajax'),
    path('', views.index, name='index'),
    path('libros/', views.listaLibros, name='listaLibros'),
    path('autores/', views.listaAutores, name='listaAutores'),
    path('editoriales/', views.listaEditoriales, name='listaEditoriales'),
    path('libros/<int:libro_id>/', views.detailLibro, name='detailLibros'),
    path('autores/<int:autor_id>/', views.detailAutor, name='detailAutores'),
    path('editoriales/<int:editorial_id>/', views.detailEditorial, name='detailEditoriales'),
]