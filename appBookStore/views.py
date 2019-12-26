from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import Libro, Editorial, Autor
from django.views.generic import TemplateView


#devuelve la portada de bookStore
def index(request):
	libros = get_list_or_404(Libro.objects.order_by('-anyo'))
	editoriales = get_list_or_404(Editorial.objects.order_by('nombre'))
	ultimosLibros = []
	for e in editoriales:
		for l in libros:
			if l.cod_editorial.id == e.id:
				ultimosLibros.append(l)
				break;

	autores = get_list_or_404(Autor.objects.order_by('nombre'))
	context = {'ultimosLibros': ultimosLibros, 'editoriales': editoriales, 'autores': autores}
	return render(request, 'index.html', context)

#devuelve los datos de un departamento
def listaLibros(request):
	libros = get_list_or_404(Libro.objects.order_by('-anyo'))
	context = {'libros': libros}
	return render(request, 'listaLibros.html', context)

def listaAutores(request):
	autores = get_list_or_404(Autor.objects.order_by('nombre'))
	context = {'autores': autores}
	return render(request, 'listaAutores.html', context)

def listaEditoriales(request):
	editoriales = get_list_or_404(Editorial.objects.order_by('nombre'))
	context = {'editoriales': editoriales}
	return render(request, 'listaEditoriales.html', context)

#devuelve los datos de un departamento
def detailLibro(request, libro_id):
	libro = get_object_or_404(Libro, pk=libro_id)
	autores = libro.autores.all()
	context = {'libro': libro, 'autores': autores}
	return render(request, 'detailLibro.html', context)

#devuelve los empelados de un departamento
def detailAutor(request, autor_id):
	autor = get_object_or_404(Autor, pk=autor_id)
	libros = get_list_or_404(Libro.objects.order_by('-anyo'))
	librosDeAutor = []
	for l in libros:
		for a in l.autores.all():
			if a.id == autor_id:
				librosDeAutor.append(l)
	context = {'autor': autor, 'librosDeAutor': librosDeAutor}
	return render(request, 'detailAutor.html', context)

	#devuelve los empelados de un departamento
def detailEditorial(request, editorial_id):
	editorial = get_object_or_404(Editorial, pk=editorial_id)
	libros = get_list_or_404(Libro.objects.order_by('-anyo'))
	librosDeEditorial = []
	for l in libros:
		if l.cod_editorial.id == editorial_id:
			librosDeEditorial.append(l)
	context = {'editorial': editorial, 'librosDeEditorial': librosDeEditorial}
	return render(request, 'detailEditorial.html', context)
	
