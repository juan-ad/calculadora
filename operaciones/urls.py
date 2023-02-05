from django.urls import path
from operaciones import views

urlpatterns = [
    path('/sumar/<int:op1>/<int:op2>', views.operar),
    path('/restar/<int:op1>/<int:op2>', views.operar),
    path('/multiplicar/<int:op1>/<int:op2>', views.operar),
    path('/dividir/<int:op1>/<int:op2>', views.operar)
]
