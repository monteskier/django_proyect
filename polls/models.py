from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Polls(models.Model):
    preguntas = models.CharField(max_length=200)
    pub_fecha = models.DateTimeField('Fecha de publicacion')
    def __str__(self):
        return self.preguntas
    def was_published_today(self):
        return self.pub_fecha.date() == datetime.date.today()
    def was_published_recently(self):
        return self.pub_fecha >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_fecha'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Publicacion reciente?'

class Opciones(models.Model):
    polls = models.ForeignKey(Polls)
    opcion = models.CharField(max_length=200)
    votes = models.IntegerField()
    def __str__(self):
        return self.opcion
