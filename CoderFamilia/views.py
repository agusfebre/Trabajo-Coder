from contextvars import Context
from django.http import HttpResponse
from django.template import Template

def familia(request):
    return HttpResponse('Esta es mi familia')

def segunda_vista(request):
    return HttpResponse ('Esta es la segunda vista de mi familia')

def apellido(self, apellido):
    texto=f'el apellido de mi familia es {apellido}'
    return HttpResponse(texto)

def viendo_template(request):
    mihtml=open('C:/Users/HP/Coder - Python/CoderFamilia/CoderFamilia/Plantilla/template.html')
    plantilla= Template(mihtml.read())
    mihtml.close()
    micontexto=Context()
    documento=plantilla.render(micontexto)
    return HttpResponse (documento)