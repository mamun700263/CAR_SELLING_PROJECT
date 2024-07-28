from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CarModel, OrderCar
from .forms import CarOrderForm
from review.forms import CommentForm

class DetailCarView(DetailView):
    """
    The main thing here will be Carmodel displayed on details page 
    the objects of carmodel will be known as car

    """
    model = CarModel
    template_name = 'cars/details.html'
    context_object_name = 'car'
    success_url=reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        """
        Get all forms mainly the comment and the buy
        """
        context = super().get_context_data(**kwargs)
        context['buy_form'] = CarOrderForm()
        context['comment_form'] = CommentForm()
        context['comments'] = self.object.comments.all()

        if self.request.method == 'POST':
            """
            check request method,
            """
            if CarOrderForm() in self.request.POST:
                buy_form = CarOrderForm(self.request.POST)
                print('hello world context data carorder')#chek korar jonno 
                if buy_form.is_valid():
                    """
                    form valid or not
                    separate the quantity for counting the actual price
                    """
                    quantity = buy_form.cleaned_data.get('quantity', 1)
                    total_price = quantity * self.object.price
                    context['total_price'] = total_price
                    buy_form.save()
        else:
            context['total_price'] = self.object.price
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'buy_form' in request.POST:
            """When you are trying to buy a car it will activate and work"""
            form = CarOrderForm(request.POST)
            print('BUY FORM WORKD')
            if form.is_valid():
                quantity = form.cleaned_data['quantity']
                if self.object.quantity >= quantity:
                    total_price = self.object.price * quantity
                    order = form.save(commit=False)
                    order.car = self.object
                    order.buyer = request.user
                    self.object.quantity -= quantity
                    self.object.owner = request.user.username
                    order.save()
                    self.object.save()
                    messages.success(request, f'You have successfully bought {quantity} {self.object.name}(s) for ${total_price}.')

                    return redirect('profile')
                else:
                    messages.error(request, 'Sorry, there are not enough cars available.')
            else:
                messages.error(request, 'Invalid form submission.')
            return self.get(request, *args, **kwargs)

def buy_car(request,car_id):
    """this function will create a history also purchase a car"""
    car = CarModel.objects.get(id = car_id)
    if request.method != 'POST':
        print('check chek car chedk')
    else:
        form = CarModel(request.POST)
        if form.is_valid():
            print(form)
    return redirect('detailview',car_id)




def comment_form(request,car_id):
    """first check if the form is sending a post request or not"""
    car = CarModel.objects.get(id = car_id)
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        # print(form.cleaned_data)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = car
            comment.save()
    return redirect('detailview',car_id)


