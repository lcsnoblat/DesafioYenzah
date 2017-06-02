from django.db import models
from django.core.urlresolvers import reverse


class Book(models.Model):
    name = models.CharField(max_length=200)
    pages = models.IntegerField()
    amount = models.IntegerField()
    limpo = models.CharField(max_length=20)
    comentario = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

        def get_absolute_url(self):
            return reverse('books_cbv:book_edit', kwargs={'pk': self.pk})
