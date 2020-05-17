from django.urls import path
from HelloWorld import views

urlpatterns = [
    path('hello-world', views.hello_world)
]
