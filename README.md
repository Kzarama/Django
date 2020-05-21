# django
![](https://lh3.googleusercontent.com/proxy/UoarSfONT7Gwd19qXjXn6SHImsEu3Q3XMlCSTJLfNob1F7tiTOeITTi_qweMBdVgfhDyMwKyDciB30xGIYm6BHgyDCG8MgZQSs55XRAnj3Y0uiZLMDf1QpVaA6d9Glx0rFq4aI_x7-D1K30ppxWUCDaMNlhhPaP-N8epwM7v3ud_7qP2LYR7rZE)

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
## Files that django create:

- init.py = declare the project like a module of python
- settings.py = define configuration of the project
- urls.py = file whit all urls of the project and redirect to the template
- wsgi.py = is the interface of the project when be in production
- manage.py = interface over the project

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