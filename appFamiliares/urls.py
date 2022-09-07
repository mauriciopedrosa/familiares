from django.urls import path
from .views import home, familiares

urlpatterns = [
    path('',home,name="home"),
    path('familiares',familiares,name="familiares"),
]
