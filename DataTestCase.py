from django.test import TestCase
from Formulario.models import Data
import datetime
from datetime import tzinfo
class DataTests(TestCase):
    def setUp(self):
        Data.objects.create(palabra = "nuevo", cantidad = 1)
        Data.objects.create(palabra = "prueba", cantidad = 11)

    def test_Son_Palabras(self):
        nuevo = Data.objects.get(palabra = "nuevo")
        prueba = Data.objects.get(palabra = "prueba")
        self.assertEqual(nuevo.palabra, "nuevo")
        self.assertEqual(prueba.palabra, "prueba")

    def test_Son_Cantidades(self):
        nuevo = Data.objects.get(palabra="nuevo")
        prueba = Data.objects.get(palabra="prueba")
        self.assertEqual(nuevo.cantidad, 1)
        self.assertEqual(prueba.cantidad, 11)
    #este test eta oensado como test de caja negra por tanto s le debe cambiar el dia , nostros lo hemos probado con el 7 de junio de 2018, en el caso de cambiar de dia
    #al ser la fecha automatica saldria error en el test

    def test_Contiene_Fecha(self):
        nuevo = Data.objects.get(palabra="nuevo")
        self.assertEqual((nuevo.fecha).ctime(), 'Thu Jun  7 00:00:00 2018' )


