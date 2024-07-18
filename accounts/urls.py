
from django.urls import path
from .views import *
urlpatterns = [
    path('registrations/',RegistrationFormView.as_view(),name='registration'),
    path('login/',LoginFormView.as_view(),name='login'),
    path('logout/',CustomLogoutView.as_view(),name='logout'),
    path('profile/',ProfileView.as_view(),name='profile'),
    path('editinfo/<int:pk>/',InformationChangeView.as_view(),name='editinfo'),

]
