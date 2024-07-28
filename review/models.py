from django.db import models
from cars.models import *
# Create your models here.
class CommentModel(models.Model):
    car = models.ForeignKey(CarModel,on_delete=models.CASCADE,related_name='comments',null=True,blank=True)
    name = models.CharField( max_length=50,verbose_name='Your Name')
    message = models.TextField(verbose_name= 'YOur message')
    time = models.DateTimeField(auto_now_add = True, null = True, blank = True)

    

    def __str__(self):
        return self.name
    