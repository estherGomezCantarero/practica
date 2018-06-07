

class TextExamples(object):

    def quitarSigno(texto):
        if type(texto) is not str :
            raise TypeError
        prohibidos = {"?", "¿", ".", ",", ";", ":", "!", "¡", "'","un","una","lo","la","el","unos","unas","-", "\"","[","]","0","1","2","3","4","5","6","7","8","9","%","$", "@","~","€","¬","¨","´","^","`","*","_","-","|"}
        return ("".join(c for c in texto.lower() if c not in prohibidos)).split()

    #def listaDePalabras(texto):
       # return quitarSigno(texto).split()

    def contar(lista):
        frecuencia = []
        for w in lista:
            frecuencia.append(lista.count(w))
        listavistos = []
        listaFinal = []
        contador = 0
        for k in lista:
            listaAux = []
            if k not in listavistos:
                listaAux.append(k)
                listavistos.append(k)
                listaAux.append(frecuencia[contador])
                listaFinal.append(listaAux)
                contador += 1
            else:
                contador += 1
        if len(listaFinal)> 3:
            for i in range(2, len(listaFinal)):
                for j in range(0,(len(listaFinal)-1)):
                    if listaFinal[j][1] > listaFinal[j+1][1]:
                        aux = listaFinal[j]
                        listaFinal[j] = listaFinal[j+1]
                        listaFinal[j+1]= aux
            listaF = []
            m = len(listaFinal)-1

            for k in range(0, (len(listaFinal))):
                listaF.insert(k,listaFinal[m])
                m = m-1
            return listaF
        else :
            return listaFinal


if __name__ == '__main__':
    my_text = "Lorem ipsum; dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut. labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    text = "This is an example text. Let us use two sentences, so that it is more logical."

    tes = "hola.. ?hola¿ hola adios  hora hola ? ¡adios"
    p="wwwalter"
    l = TextExamples.quitarSigno(tes)
    k = TextExamples.contar(l)
    print(TextExamples.contar(p))
    print(TextExamples.quitarSigno(p))
    print(k[0][0])
    #l2= TextExamples.quitarSigno(my_text)
    #print(TextExamples.contar(l2))