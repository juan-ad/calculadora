from django.urls import path
from operaciones import views

urlpatterns = [
    path('/sumar/<op1>/<op2>', views.sumar),
    path('/restar/<op1>/<op2>', views.restar),
    path('/multiplicar/<op1>/<op2>', views.multiplicar),
    path('/dividir/<op1>/<op2>', views.dividir)
]
