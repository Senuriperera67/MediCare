from django.urls import path
from . import views

urlpatterns = [
    path('addtransaction/', views.add_transaction, name='add_transaction'),
    
    
]