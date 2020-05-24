# django
![](img/django.png)

---

For work with django is required have installed python3
## To create virtual envirnment (venv)
For create a virtual environment
~~~bash
python3 -m venv NAMEVENV
~~~
Activate venv in linux
~~~bash
source NAMEVENV/bin/activate
~~~
Activate venv in windows
~~~bash
NAMEVENV/Scripts/activate
~~~
For deactivate venv
~~~bash
deactivate
~~~

---

## To create a project
To install django run in console
~~~bash
pip install django -U
~~~
### Commands of django
To see the commands of django
~~~bash
django-admin
~~~
To start a project
~~~bash
django-admin startproject NAMEPROJECT .
~~~

---

## Templates
Presentation of the data in HTML
Make a new folder in the app
- render = receive a request, the template
---

## Application in django
Is a set of code that is responsible of a specific part of the project
start application over a project
~~~bash
manage.py startapp NAME_APPLICATION
~~~
Install an application
- In INSTALLED_APPS in settings.py of the project add NAME_APPLICATION

---

## DB
django uses ORM(Object-Relational Mapping) for make the tables of the db, allow the access and control of a relational db through an abstraction of classes and objects  
Models = part of the projects that structure the tables and the properties
### Migrations
Migrate changes
~~~bash
manage.py makemigrations
~~~
Causes all changes to be saved in the db    
~~~bash
manage.py migrate
~~~
Finally of migrate changes run migrate for save the changes in the db
create 
## Create a model user
Run the shell of python
~~~bash
manage.py shell
~~~
import the model user of contrib
~~~bash
from django.contrib.auth.models import User
~~~
create a new user
~~~bash
user = User.objects.create_user(username='Kevin', password='123')
~~~
create a superuser
~~~bash
manage.py createsuperuser
~~~

---

## Middleware
validate a session of an user

---

## Files that django create:
- init.py = declare the project like a module of python
- settings.py = define configuration of the project
- urls.py = file whit all urls of the project and redirect to the template
- wsgi.py = is the interface of the project when be in production
- manage.py = interface over the project relationated with the settings of the project
### Variables in settings-py
- BASE_DIR = the path of the project
- SECRET_KEY= for the passwords and sessions of db
- DEBUG = shows that the project is in development (debug mode)
- ALLOWED_HOST = the host that have permissions to interact with the project
- INSTALLED_APPS = applications installed in the project
- MIDDLEWARE = intermediaries in django
- ROOT_URLCONF = define the module of urls
- TEMPLATES = configuration of templates
- WSGI_APPLICATION = file of wsgi
- DATABASES = configuration of the db
- AUTH_PASSWORD_VALIDATORS = validations of passwords
- LANGUAGE_CODE = language of the application
- TIME_ZONE = time zone of the application
- USE_I18N = translate
- USE_L10N = translate
- USE_TZ = timezone library
- STATIC_URL = resolve whit the static file query
## Files created in a application
- __init.py__ (migrations) = record the changes in the db
- admin.py = registers the models in the administrator of django
- apps.py = declare the configuration of the app 
- models.py = define the models of data
- test.py = for test
- views.py = is the responsible of business logic and allow the connection between the template and the models

---

## Commands
To see the commands of the manage and each application
~~~bash
manage.py
~~~
Run the server
~~~bash
manage.py runserver
~~~
shell of python with djangp
~~~bash
manage.py shell
~~~