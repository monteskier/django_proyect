from django.db import models
import datetime

# Create your models here.
class Polls(models.Model):
    preguntas = models.CharField(max_length=200)
    pub_fecha = models.DateTimeField('Fecha de publicacion')
    def __str__(self):
        return self.preguntas
    def was_published_today(self):
        return self.pub_fecha.date() == datetime.date.today()

class Opciones(models.Model):
    polls = models.ForeignKey(Polls)
    opcion = models.CharField(max_length=200)
    votes = models.IntegerField()
    def __str__(self):
        return self.opcion
