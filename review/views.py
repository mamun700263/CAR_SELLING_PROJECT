from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

#from this folder
from .models import *
from .forms import *



def add_comment(request):
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cars:detailview')
    return render(request,'cars/details.html')