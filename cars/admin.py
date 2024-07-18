from django.contrib import admin
from  .models import *
# Register your models here.
admin.site.register(BrandModel)
admin.site.register(CarModel)
admin.site.register(OrderCar)