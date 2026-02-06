from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
from category.models import Category
# Create your views here.
def product_list(request):
    cat=Category.objects.all()
    return render(request,"products.html",{'category':cat})
def product_create(request):
    return HttpResponse("ProductCreate")
def product_delete(request,id):
    return HttpResponse("ProductDelete")
def product_update(request):
    return HttpResponse("ProductUpdate")
def product_edit(request):
    return HttpResponse("ProductEdit")