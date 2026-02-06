from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.category_list,name='category_list'),
    path('category_create/',views.category_create,name='category_create'),
    path('category_edit/<int:id>',views.category_edit,name='category_edit'),
    path('category_delete/<int:id>',views.category_delete,name='category_delete'),
]
