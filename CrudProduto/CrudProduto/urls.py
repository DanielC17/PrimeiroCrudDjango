
from django.urls import path
from CrudProduto import views

urlpatterns = [
    path('produto/', views.produto),
    path('addProduto/', views.addProduto),
    
]
