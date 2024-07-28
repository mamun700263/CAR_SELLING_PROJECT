from django.db import models
from django.contrib.auth.models import User
# from .models import CarModel
# Create your models here.


class BrandModel(models.Model):
    """
    there will be a brand name only
    """
    name = models.CharField(max_length=100,unique=True,verbose_name= 'Car Brand ')
    def __str__(self):
        return self.name
    


class CarModel(models.Model):
    """
    for foreign key if the foreign key is in the same folder first make that then set it 
    """
    name = models.CharField(max_length=100,verbose_name='Car Name')
    brand = models.ForeignKey(BrandModel,on_delete=models.CASCADE)
    image = models.URLField(verbose_name='Photo Url')
    price = models.PositiveIntegerField(verbose_name='Price')
    quantity = models.PositiveIntegerField(verbose_name='Cars Available',blank=True,null=True)
    detail = models.TextField(verbose_name='Details',null=True,default='Sorry ')
    owner = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.name
    



class OrderCar(models.Model):
    car = models.ForeignKey(CarModel,on_delete=models.CASCADE,verbose_name='ordered car')
    buyer = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Buyer name')
    time = models.DateField(auto_now_add=True)
    quantity = models.PositiveIntegerField(verbose_name='Quantity',default=1)

    def __str__(self):
        return f'{self.car} and {self.buyer}'
    


    