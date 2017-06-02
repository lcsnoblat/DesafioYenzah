from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from music_cbv.models import Music

class MusicList(ListView):
    model = Music

class MusicCreate(CreateView):
    model = Music
    fields = ['name', 'band','amount','limpo','comentario']
    success_url = reverse_lazy('music_cbv:music_list')

class MusicUpdate(UpdateView):
    model = Music
    fields = ['name', 'band','amount','limpo','comentario']
    success_url = reverse_lazy('music_cbv:music_list')

class MusicDelete(DeleteView):
    model = Music
    success_url = reverse_lazy('music_cbv:music_list')
