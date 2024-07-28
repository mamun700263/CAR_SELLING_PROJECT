
from django.urls import path
from .views import *

appname = 'accounts'
urlpatterns = [
    #Registration form
    path('registrations/',RegistrationFormView.as_view(),name='registration'),
    #login form
    path('login/',LoginFormView.as_view(),name='login'),
    #log out url that will take to login again
    path('logout/',CustomLogoutView.as_view(),name='logout'),
    #profile page
    path('profile/',ProfileView.as_view(),name='profile'),
    #user informations changing page
    path('editinfo/<int:pk>/',InformationChangeView.as_view(),name='editinfo'),

]
