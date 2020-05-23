from Examples import views
from django.urls import path

urlpatterns = [

    path('sort/', views.sort_ints),
    path('hi/<str:name>/<int:age>/', views.say_hi),
    
]
