from django.urls import path
from . import views

urlpatterns=[
    path ('patienthome/', views.patient_home, name = 'patient_home'),
   

]