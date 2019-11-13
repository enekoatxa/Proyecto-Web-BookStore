from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import Libro, Editorial, Autor


#devuelve la portada de bookStore
def index(request):
	# libros = get_list_or_404(Libro.objects.order_by('anyo').groupBy(editorial))
	libros = Libro.objects.raw('SELECT * FROM libros ORDER BY anyo GROUP BY editorial')
	editoriales = get_list_or_404(Departamento.objects.order_by('nombre'))
	autores = get_list_or_404(Departamento.objects.order_by('nombre'))
	context = {'libros': libros, 'editoriales': editoriales, 'autores': autores}
	return render(request, 'index.html', context)

#devuelve los datos de un departamento
def listaLibros(request):
	libros = get_list_or_404(Libro.objects.order_by('anyo'))
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
	return render(request, 'detailLibro', context)

#devuelve los empelados de un departamento
def detailAutor(request, autor_id):
	autor = get_object_or_404(Autor, pk=autor_id)
	context = {'autor': autor}
	return render(request, 'detailAutor', context)

	#devuelve los empelados de un departamento
def detailEditorial(request, editorial_id):
	editorial = get_object_or_404(Editorial, pk=editorial_id)
	context = {'editorial': editorial}
	return render(request, 'detailEditorial', context)
	
