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

    def test_Contiene_Fecha(self):
        nuevo = Data.objects.get(palabra="nuevo")
        self.assertEqual((nuevo.fecha).ctime(), 'Wed Jun  6 00:00:00 2018' )
