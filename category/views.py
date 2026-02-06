from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import Category
# Create your views here.
def category_list(request):
    data=Category.objects.all()
    categories = Category.objects.select_related('parent_category').all()
    return render(request, 'category.html', {'categories': categories,'category':data})
def category_create(request):
    if request.method=="POST":
        title=request.POST['txtCategoryName']
        pcategory_id=request.POST['selParent']
        if(pcategory_id=="select"):
            cat=Category(title=title)
            cat.save()
        else:
            cat=Category(title=title,parent_category_id=pcategory_id)
            cat.save()
    return redirect('category_list')
def category_edit(id):
    return HttpResponse('edit')
def category_delete(id):
    return HttpResponse('delete')