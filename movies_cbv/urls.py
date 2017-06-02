from django.conf.urls import patterns, url

from movies_cbv import views

urlpatterns = patterns('',
  url(r'^$', views.MovieList.as_view(), name='movie_list'),
  url(r'^new$', views.MovieCreate.as_view(), name='movie_new'),
  url(r'^edit/(?P<pk>\d+)$', views.MovieUpdate.as_view(), name='movie_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.MovieDelete.as_view(), name='movie_delete'),
)
