from django.db import models
from category.models import Category
# Create your models here.
class Products(models.Model):
    name=models.CharField(max_length=100,unique=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TextField(blank=True,null=True)
    stock=models.IntegerField()
    images=models.TextField()
    catid=models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
    )
    def __str__(self):
        return self.name