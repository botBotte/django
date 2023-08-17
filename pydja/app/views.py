from django.shortcuts import render

# Create your views here.

def landingview(request):
    return render(request, 'landing.html')

def productview(request):
    return render(request, 'productlist.html')

def suppliersview(request):
    return render(request, 'suppliers.html')

