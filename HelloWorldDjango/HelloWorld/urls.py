from HelloWorld import views
from django.urls import path

urlpatterns = [
    path('hello-world/', views.hello_world),
]
