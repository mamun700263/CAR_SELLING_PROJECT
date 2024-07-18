"""
URL configuration for CarSelling project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from accounts.views import HomeView
"""
all apps will be included and only the home page will be here from accounts app 
1.accounts will be for just signup,login,home view
2.cars willl contain the brands and cars with model and everything related to them
3.review will contain the review,comment model and some more
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('cars/',include('cars.urls')),
    path('review/',include('review.urls')),
    path('',HomeView.as_view(),name='home'),
    path('cars/<str:brand>/',HomeView.as_view(),name='home2'),
]
