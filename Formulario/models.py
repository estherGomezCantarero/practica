from django.db import models
from datetime import date
class Data(models.Model):

    palabra = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(default = date.today)


    def masUsadas(self):
        tresmayores = Data.objects.order_by('fecha').order_by('cantidad').reverse()[:3]
        return tresmayores
    def __str__(self):
        template = '{0.palabra} {0.cantidad} {0.fecha}'
        return template.format(self)
