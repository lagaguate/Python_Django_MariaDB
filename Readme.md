
# Python_Django_MariaDB
Ejercicion Python + Django + Maria DB, curso con el canal  de Youtube de Pildoras Informativas

## Configuración entorno desarrollo
1. Crear entorno virtual con Conda (Si ya existe para Django activar
- Ver que versiones disponbles tiene Conda:  conda search python
```sh
conda create -n django python=3.10
```
2. Activar entorno virtual Conda
```sh
conda activate django
```
3. Instalar Django en el entorno virtual django
```sh
conda install -c anaconda django -n django
```
4. Se presume que tienes instalado visual Studio, entonces:
4.1 Crear carpeta de trabajo
4.2 Abrir visual studio 
```sh
code .
```

## Creacion de proyecto con Django

1.  Creacion Proyecto
```sh
django-admin startproyect TiendaOnline
```

2. Crear proyecto
```sh
Cd TiendaOnline
python3 manage.py startapp gestionPedidos
```

3. Chequer inclusion de la aplicacion
```sh
python3 manage.py check gestionPedidos
```
4. Crear la BD
```sh
python3 manage.py makemigrations
```
#  gestionPedidos/migrations/0001_initial.py

5. Indicar que crear la tablas.  Debe poner el numbero generado en el paso 4
```sh
python3 manage.py sqlmigrate gestionPedidos 0001
```
6- crear los objeto en la bd sqlite3
```sh
python manage.py migrate
```