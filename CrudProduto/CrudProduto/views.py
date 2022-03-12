
from django.http import HttpResponse
from django.shortcuts import render

def produto(request):
    return render(request, "index.html")