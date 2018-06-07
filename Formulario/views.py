from django.shortcuts import render
from Formulario.models import Data
from sample import text_examples
import urllib.request
from bs4 import BeautifulSoup

def vistaFormulario(request):

    text = ''
    submitbutton = ''
    if request.method =='POST':
        text = request.POST.get('text')
        submitbutton = request.POST.get('Submit')

        m=str(text)

        #descarga el contenido del html

        with urllib.request.urlopen(text) as response:
            page = response.read()
        soup = BeautifulSoup(page, 'html.parser')
        p= soup.find_all('p')
        h=[]
        for a in p:
            h.append(a.text.split())
        articulo=str(h)

        n = text_examples.TextExamples.quitarSigno(articulo)
        k = text_examples.TextExamples.contar(n)
        #Data.objects.all().delete()
        for objeto in range(0, len(k)):
            lista = Data.objects.values_list('palabra', flat= True).order_by('id')
            o=k[objeto][0]
            if o in lista:

                valorAnterior = Data.objects.get(palabra= k[objeto][0]).cantidad
                valorAnterior+= k[objeto][1]
                Data.objects.filter(palabra = k[objeto][0]).update(cantidad = valorAnterior)
                pass
            else:
                dato = Data.objects.create(palabra = k[objeto][0], cantidad = k[objeto][1])
                dato.save()

        #tresmayores = Data.objects.masUsadas()


        context = {'text': text,
                    'submitbutton': submitbutton,
                    'type':k

                    }

        return render(request, 'form/form.html', context)

    context = {'text': text,
               'submitbutton': submitbutton,
               'type': text,

               }

    return render(request, 'form/form.html', context)


#Data.objects.get(palabra = 'de')






  


