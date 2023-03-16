
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
6. crear los objeto en la bd sqlite3
```sh
python3 manage.py migrate
```
7. Ingresar al shell de Django, por medio del Shell insertar resitros a Articulos
```sh
python3 manage.py shell
- Como importar el modelo Articulos
>>> from gestionPedidos.models import Articulos
- Como insertar valores
>>> art = Articulos(nombre='Laptop', seccion='Informatica', precio=90)
- Se debe hacer commit con saves
>>> art.save()
>>> art = Articulos(nombre='Mouse', seccion='Informatica', precio=10.15)
- Crear articulos sin usar save(), y graba directo a la BD
>>> art = Articulos.objects.create(nombre='Teclado', seccion='Informatica', precio=30.50)
```
8. Actualizar un registro con Shell (python3 manage.py shell)
```sh
art.precion(111.50)
art.save()
```
9.  Borrar un registros con Shell (python3 manage.py shell)
```sh
art5 = Articulos.objects.get(id=2)
art5.delete()
- Consultar registros
- Recupera la query
lista.query.__str__()
```
# Crecion de BD PostgresSql
- Hemos instalado postgres y pgadmin4 en docker separados
- Hemos creado la Bd de TiendaOnline

# Otros componentes de Django
1. Instalar psycopg2

# Instrucciones para crear un usuario en Postgres
```sh
CREATE USER usrtienda WITH PASSWORD 'usrtienda';
GRANT ALL PRIVILEGES ON DATABASE tiendaonline to usrtienda;
GRANT ALL ON SCHEMA public TO usrtienda;
```

# Servidor Web DJango 
1. Levantar el servidor web de Django
```sh
python3 manage.py runserver
```
2. Acceder a la administracion de Django (localhost)
```sh
http://127.0.0.1:8000/admin/login/?next=/admin/
```
3. Crear Super usuario de Django
```sh
python manage.py createsuperuser
```
- usuario: lagaguate
- email: lagaguate
. pass: hunter1972

4. Actualizar password de superusuario
```sh
python3 manage.py changepassword lagaguate
```

# Actualizacion de estructura
- Cuando se modifique el modelo se debe ejecutar esto
- python3 manage.py makemigrations
- Luego esto otro python3 manage.py migrate
- y con esto ya tenemos actualizado el objeto