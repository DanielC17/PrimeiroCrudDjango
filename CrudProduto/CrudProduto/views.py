
from django.http import HttpResponse
from django.shortcuts import render
from CrudProduto.entity import class_produto

produto1 = class_produto(1, "Tênis Nike ", "Tenis para basquete", 300.00 , 10)
produto2 = class_produto(2, "Tênis Adidas", "Tenis para corrida", 230.00, 27)
produto3 = class_produto(2, "Tenis Puma", "Tenis para skate", 280.00, 30)

lista_produtos = [produto1, produto2, produto3]



def produto(request):
    return render(request, "index.html", {"lista_produtos":lista_produtos})