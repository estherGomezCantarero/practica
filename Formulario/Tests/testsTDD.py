import unittest
from sample.text_examples import TextExamples


class TestStringsExamples(unittest.TestCase):

    def test_quitarInterrogacion(self):
        string1="hola?"
        result=TextExamples.quitarSigno(string1)

        assert result == ['hola']

    def test_quitarExclamacion(self):
        string1 = "adios!"
        result = TextExamples.quitarSigno(string1)
        assert result == ['adios']

    def test_quitarUn(self):
        string1="un perro"
        result=TextExamples.quitarSigno(string1)
        assert result ==['un', 'perro']

    def test_quitarPuntoComa(self):
        string1="hola;"
        result=TextExamples.quitarSigno(string1)
        assert result == ['hola']

    def test_quitarDosPuntos(self):
        string1="hola:"
        result=TextExamples.quitarSigno(string1)
        assert result ==['hola']

    def test_quitarNumero(self):
        string1 = "hola2"
        result = TextExamples.quitarSigno(string1)
        assert result == ['hola']

    def test_quitar2Numeros(self):
        string1 = "h2ola2"
        result = TextExamples.quitarSigno(string1)
        assert result == ['hola']


    def test_quitarCara(self):
        string1 = "hola¬"
        result = TextExamples.quitarSigno(string1)
        assert result == ['hola']

    def test_contar2Letras(self):
        string1="perro perro perro a a "
        result=TextExamples.contar(string1)
        assert result ==[['r', 6], [' ', 5], ['o', 3], ['e', 3], ['a', 2], ['p', 3]]

    def test_contar3Letras(self):
        string1="wwwalter"
        result=TextExamples.contar(string1)
        print(result)
        assert result == [['w', 3], ['r', 1], ['e', 1], ['t', 1], ['l', 1], ['a', 1]]


if __name__ == '__main__':
    unittest.main()