from django.urls import path
from . import views

urlpatterns=[
    path ('medihome/', views.medicine_home, name = 'medicine_home'),
    

]