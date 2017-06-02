from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from movies_cbv.models import Movie

class MovieList(ListView):
    model = Movie

class MovieCreate(CreateView):
    model = Movie
    fields = ['name', 'director','amount','limpo','comentario']
    success_url = reverse_lazy('movies_cbv:movie_list')

class MovieUpdate(UpdateView):
    model = Movie
    fields = ['name', 'director','amount','limpo','comentario']
    success_url = reverse_lazy('movies_cbv:movie_list')

class MovieDelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('movies_cbv:movie_list')
