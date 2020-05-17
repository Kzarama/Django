# Django

## To create a project
```bash

Install python3
pip install django -U
django-admin = to see the commands of django
django-admin startproject NAMEPROJECT .
```

## To create venv

```bash
python3 -m venv NAMEVENV
source NAMEVENV/bin/activate
deactivate
```

## Files that django create:

- __init.py__ = declare the project like a module of python
- settings,py = define configuration of the project
- urls.py = file whit all urls of the project and redirect to the template
- wsgi.py = is the interface of the project when be in production
- manage.py = interface over the project

## settings-py

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

## Commands

- python3 manage.py = to see the commands of the manage and each application
- python3 manage.py runserver = run the server