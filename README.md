PASOS:

Entrar en consola Bash:

1.- Crear entorno virtual

virtualenv env

2.- Instalar Django en el entorno

//Para versión específica p.ej. pip install -U django==4.1.6 
ó pip install django para la última versión

3 - Ejecutar el proyecto

python manage.py runserver

4 - Rutas

localhost:8000/calculadora/sumar/2/2
localhost:8000/calculadora/restar/2/2
localhost:8000/calculadora/multiplicar/2/2
localhost:8000/calculadora/dividir/2/2