from django.http import HttpResponse
import datetime

def saludo(request):
    return HttpResponse("Hola mundo es mi primera paguina en django")

def despedida(request):
    return HttpResponse("Me despidode ustedes")
def horaactual(request):
    feca_actual = datetime.datetime.now()
    
    documento = """<html>
    <body>
    <h1>
    fecha y hora actual %s
    </h1>
    </body>
    </html>""" %feca_actual
    
    return HttpResponse(documento)

def calculaEdad(request,agno,edad):
    periodo =agno-2023
    edadFutura = edad + periodo
    
    documento = """<html>
    <body>
    <h2>
    En el año %s tendras %s años 
    </h2>
    </body>
    </html>
    """%(agno,edadFutura)
    
    return HttpResponse(documento)    
    