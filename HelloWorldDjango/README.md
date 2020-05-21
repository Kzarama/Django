# Hello World
Then of create a proyect, create a new file called "views.py" inside of the folder, and inside put

~~~python
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('Hello world!')
~~~

In the urls.py put for link the new view

~~~python
from HelloWorld import views
from django.urls import path

urlpatterns = [
    path('hello-world/', views.hello_world)
]
~~~

and run in the bash
~~~bash
manage.py runserver
~~~