from django.db import models
from django.core.urlresolvers import reverse


class Movie(models.Model):
    name = models.CharField(max_length=200)
    director =  models.CharField(max_length=200)
    amount = models.IntegerField()
    limpo = models.CharField(max_length=20)
    comentario = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

        def get_absolute_url(self):
            return reverse('movies_cbv:movie_edit', kwargs={'pk': self.pk})
