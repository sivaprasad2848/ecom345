from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Products
from category.models import Category
from django.core.files.storage import FileSystemStorage
# Create your views here.
def product_list(request):
    cat=Category.objects.all()
    products=Products.objects.all()
    return render(request,"products.html",{'category':cat,'products':products})
def product_create(request):
    if request.method=="POST":
        name=request.POST['txtPname']
        category_id=request.POST['selCategory']
        price=request.POST['txtUnitprice']
        stock=request.POST['txtStock']
        desc=request.POST['txtDesc']
        file=request.FILES['filImage'] if 'filImage' in request.FILES else None
        fileurl=""
        if file:
            fs=FileSystemStorage()
            file=fs.save(file.name,file)
            fileurl=fs.url(file)
        category = Category.objects.get(id=category_id)
        p=Products(name=name,catid=category,price=price,stock=stock,description=desc,images=fileurl)
        p.save()
    return redirect('product_list')
def product_delete(request,id):
    return HttpResponse("ProductDelete")
def product_update(request):
    return HttpResponse("ProductUpdate")
def product_edit(request):
    return HttpResponse("ProductEdit")