from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

#from this folder
from .models import *
from .forms import *



# Create your views here.


# class CommentFormView(CreateView):
#     model = CommentModel
#     form_class = CommentForm
#     template_name = 'accounts/forms.html'
#     # success_url = ''

