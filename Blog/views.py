from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from Blog.forms import PostFormulario
from Blog.models import Post

def inicio(request):
    return render(request,'Blog/post_list.html')

def categoria(request):
    return render(request,'Blog/categoria.html')

def post(request):
    return render(request,'Blog/post.html')

def postFormulario(request):
    if request.method == 'POST':

        formulario = PostFormulario(request.POST)
        print(formulario)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            
            autor = informacion['autor']
            titulo= informacion['titulo']
            resumen = informacion['resumen']
            contenido = informacion['contenido']
            imagen = informacion['imagen']
            fecha = informacion['fecha']
            categoria = informacion['categoria']

            post = Post(autor=autor, titulo=titulo, resumen=resumen, contenido=contenido, imagen=imagen, fecha=fecha, categoria=categoria)
            post.save()

        return render(request, 'Blog/inicio.html')

    else:
        formulario = PostFormulario()

    return render(request, 'Blog/postFormulario.html', {'formulario': formulario})

def busquedaCategoria(request):
    return render(request, 'Blog/busquedaCategoria.html')

def buscar(request):
    #respuesta = f"Estoy buscando la categoría: {request.GET['categoria'] }"
   # if request.GET['categoria']:
    #    categoria = request.GET['categoria']
     #   post = Post.objects.filter(categoria__icontains= categoria)
   # return render(request, 'Blog/resultadosBusqueda.html', {"post": post, "categoria":categoria})
   # else: 
   #     respuesta = "No enviaste datos"

    return HttpResponse(respuesta)

def about(request):
    return render(request, 'Blog/about.html')

def padre(self):
    plantilla = loader.get_template('padre.html')
    documento = plantilla.render()
    return HttpResponse(documento)

#-----------------------
class PostList(ListView):
    model = Post
    template_name = 'Blog/post_list.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'Blog/post_detail.html'

class PostCreate(CreateView):
    model = Post
    success_url = reverse_lazy('post_list')
    fields = ['autor', 'titulo','resumen', 'contenido', 'fecha', 'categoria']

class PostUpdate(UpdateView):
    model = Post
    success_url = reverse_lazy('post_list')
    fields = ['autor', 'titulo','resumen', 'contenido', 'fecha', 'categoria']

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')