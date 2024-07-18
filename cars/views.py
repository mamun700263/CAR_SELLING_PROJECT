# from typing import Any
# from django.shortcuts import render,redirect
# from django.urls import reverse_lazy
# #from geniric
# from django.views.generic import DetailView,CreateView
# from django.views.generic.edit import FormMixin
# # from contrib
# from django.contrib import messages
# # from this folder
# from .models import *
# from .forms import CarOrderForm
# #from other folders
# from review.models import CommentModel
# from review.forms import CommentForm

# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from .models import CarModel, OrderCar
# # from .forms import OrderCarForm

# class DetailCarView(DetailView):
#     model = CarModel
#     template_name = 'cars/details.html'
#     context_object_name = 'car'
#     success_url = reverse_lazy('home')

#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     buy_form = CarOrderForm
#     #     context['buy_form'] = buy_form
#     #     context["comment_form"] = CommentForm 
#     #     context["comments"] = self.object.comments.all()

#     #     total_price= 0 ;
#     #     if 'quantity' in buy_form:
#     #         total_price = context['buy_form'].initial.get('quantity', 1) * self.object.price

#     #     context['total_price']=total_price
#     #     return context


#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         buy_form = CarOrderForm()
#         context['buy_form'] = buy_form
#         context["comment_form"] = CommentForm()
#         context["comments"] = self.object.comments.all()
#         context['total_price'] =self.object.price

#         if self.request.method == 'POST':
#             buy_form = CarOrderForm(self.request.POST)
#             context['total_price'] =self.object.price
#             if buy_form.is_valid():
#                 quantity = buy_form.cleaned_data.get('quantity', 1)
#                 context['total_price'] = quantity * self.object.price
#                 buycar(self.request,CarOrderForm.id)
#         return context



#     def post(self,request,*args,**kwargs):
#         self.object = self.get_object()
#         if 'comment_form' in request.POST:
#             form = CommentForm(request.POST)
#             if form.is_valid():
#                 comment = form.save(commit=False)
#                 comment.car = self.object
#                 comment.save()
#                 return self.get(request,*args,**kwargs)
#         else:
#             buy_car = CarOrderForm()
#             if buy_car.is_valid():
#                 new_car = buy_car.save(commit=False)
#                 qu = new_car.quantity
#                 new_car.car = self.object
#                 new_car.buyer = request.user
#                 new_car.save()
#                 return redirect('home')
#         return self.get(request,*args,**kwargs)








# # def buycar(request,pk):
# #     """
# #     we will first check if car is available or not
# #     """
# #     car = CarModel.objects.get(pk=pk)
# #     buy_form = CarOrderForm()
# #     if car.quantity>=1:
# #         car.quantity -= 1
# #         messages.success(request,'Your Bought the Car')
# #         car.owner = request.user.username
# #         buy_form.buyer = request.user.username
# #         buy_form.car = car
# #         buy_form.save;
# #         car.save()
# #         return redirect('profile')

# #     else:
# #         messages.info(request,'Sorry Car not available')
# #         return redirect('home')

# def buycar(request, pk):
#     """
#     Check if the car is available in the required quantity and handle the purchase process.
#     """
#     car = get_object_or_404(CarModel, pk=pk)
#     if request.method == 'POST':
#         form = CarOrderForm(request.POST)
#         if form.is_valid():
#             quantity = form.cleaned_data['quantity']
#             if car.quantity >= quantity:
#                 total_price = car.price * quantity
#                 order = form.save(commit=False)
#                 order.car = car
#                 order.buyer = request.user
#                 car.quantity -= quantity
#                 car.owner = request.user.username
#                 order.save()
#                 car.save()
#                 messages.success(request, f'You have successfully bought {quantity} {car.name}(s) for ${total_price}.')
#                 return redirect('profile')
#             else:
#                 messages.error(request, 'Sorry, there are not enough cars available.')
#         else:
#             messages.error(request, 'Invalid form submission.')
#     else:
#         form = CarOrderForm()

#     return render(request, 'cars/details.html', {'car': car, 'form': form})


from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CarModel, OrderCar
from .forms import CarOrderForm
from review.forms import CommentForm

class DetailCarView(DetailView):
    model = CarModel
    template_name = 'cars/details.html'
    context_object_name = 'car'
    success_url = reverse_lazy('home')
    def get_context_data(self, **kwargs):
        # Call the superclass method to get the initial context
        context = super().get_context_data(**kwargs)

        # Add the buy_form, comment_form, and comments to the context
        context['buy_form'] = CarOrderForm()
        context['comment_form'] = CommentForm()
        context['comments'] = self.object.comments.all()

        # Check if the request method is POST
        if self.request.method == 'POST':
            # Create an instance of CarOrderForm with POST data
            buy_form = CarOrderForm(self.request.POST)
            print('hello world')

            # Check if the form is valid
            if buy_form.is_valid():
                # Get the quantity from the cleaned data of the form
                quantity = buy_form.cleaned_data.get('quantity', 1)
                # Calculate the total price based on quantity and car price
                total_price = quantity * self.object.price
                # Add total_price to the context
                context['total_price'] = total_price
                # Print the quantity and a debug message
                print(f"Quantity: {total_price}")
                print('hello world')
            # else:
            #     print('form is invalid')
        else:
            # If not a POST request, set the total_price to default car price
            context['total_price'] = self.object.price
            print('quantity not post')

        # Return the updated context
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'comment_form' in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.car = self.object
                comment.save()
                return self.get(request, *args, **kwargs)

        elif 'buy_form' in request.POST:
            form = CarOrderForm(request.POST)
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
                    return redirect('profile', total_price=total_price)
                else:
                    messages.error(request, 'Sorry, there are not enough cars available.')
            else:
                messages.error(request, 'Invalid form submission.')

        return self.get(request, *args, **kwargs)
