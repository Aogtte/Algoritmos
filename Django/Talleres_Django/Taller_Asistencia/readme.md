## Sistema de Asistencias 

Aplicación web desarrollada con Django para registrar y listar asistencias almacenados en una base de datos utilizando Postgres(Nexus) y desplegada en Render.

## TecnologÃ­as
- Python
- Django
- Postgres
- HTML
- Render
- Git y GitHub

## Funcionalidades
- Listado de asistencias.
- Registro de nuevas asistencias.
- Crud de asistencias.
- Validación de campos.
- Almacenamiento en nube mediante Postgres.

## Ejecución en Windows CMD

```cmd

python -m venv venv
venv\scripts\activate
pip install django

pip install psycopg[binary] dj-database-url python-dotenv

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```



## Git

```cmd
git init
git add .
git commit -m "Se actualiza el proyecto"
git branch -M main
git remote add origin https://github.com/Aogtte/Taller_Asistencia.git
git push -u origin main
```