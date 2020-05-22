from Examples import views
from django.urls import path

urlpatterns = [
    path('sort/', views.sort_ints),
]
