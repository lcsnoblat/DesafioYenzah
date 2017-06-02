from django.conf.urls import patterns, url

from music_cbv import views

urlpatterns = patterns('',
  url(r'^$', views.MusicList.as_view(), name='music_list'),
  url(r'^new$', views.MusicCreate.as_view(), name='music_new'),
  url(r'^edit/(?P<pk>\d+)$', views.MusicUpdate.as_view(), name='music_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.MusicDelete.as_view(), name='music_delete'),
)
