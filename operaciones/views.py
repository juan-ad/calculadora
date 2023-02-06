from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sumar(request, op1, op2):
    try:
        context = { 'title': 'SUMA', 'result': f' {op1} + {op2} = { int(op1) + int(op2) }' }
        response = render(request, 'calculadora.html', context)
    except:
        response = render(request, 'error.html', {'error': "Error en el tipo de dato"})
    return response

def restar(request, op1, op2):
    try:
        context = { 'title': 'RESTA', 'result': f' {op1} - {op2} = { int(op1) - int(op2) } ' }
        response = render(request, 'calculadora.html', context)
    except:
        response = render(request, 'error.html', {'error': "Error en el tipo de dato"})
    return response

def multiplicar(request, op1, op2):
    try:
        context = { 'title': 'MULTIPLICACIÓN', 'result': f' {op1} * {op2} = { int(op1) * int(op2) } ' }
        response = render(request, 'calculadora.html', context)
    except:
        response = render(request, 'error.html', {'error': "Error en el tipo de dato"})
    return response

def dividir(request, op1, op2):
    try:
        context = { 'title': 'DIVISIÓN', 'result': f' {op1} / {op2} = { int(op1) / int(op2) } ' }
        response = render(request, 'calculadora.html', context)
    except ZeroDivisionError:
        response = render(request, 'error.html', {'error': "División por cero"})
    except:
        response = render(request, 'error.html', {'error': "Error en el tipo de dato"})
    return response