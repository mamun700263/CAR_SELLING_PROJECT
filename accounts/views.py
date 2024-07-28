from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView,ListView
from django.views.generic.edit import UpdateView
from django.contrib.auth.views import LogoutView,LoginView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
#from different folder
from cars.models import CarModel,BrandModel,OrderCar
from django.urls import reverse_lazy
from .forms import *
# Create your views here.



class RegistrationFormView(CreateView):
    """
    You have to make a Form by your self to get desired informations
    i created RegistrationForm where i will be asking for first and last name with email and user name and pass will be automatically therer

    """

    form_class  = RegistrationForm 
    template_name = 'accounts/form.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request,'Account Registrations Successfull. Please Log in')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request,'Account Registration failed. Please Try again')
        return response

    def get_context_data(self, **kwargs):
        """
        to know more about the form
        """
        context = super().get_context_data(**kwargs)
        context["form_type"] = 'Registration'
        return context
    



class LoginFormView(LoginView):
    """
    only registered users are able to login with username and password
    """
    model = User
    form_class = AuthenticationForm
    template_name = 'accounts/form.html'
        
    def form_valid(self, form):
        messages.success(self.request,' Successfully logged in')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request,' Please Try again')
        return response
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_type"] = 'Login'
        return context



@method_decorator(login_required(login_url='login'),name='dispatch')
class InformationChangeView(UpdateView):
    """
    no need of a form 
    just use the fields
    """
    model = User
    fields = ['username','first_name','last_name','email']
    template_name = 'accounts/form.html'
    success_url = reverse_lazy('profile')



@method_decorator(login_required(login_url='login'), name='dispatch')
class CustomLogoutView(LogoutView):
    """
    be sure you used the link as a action in a form inside which there will be a button typed as submit
    """
    next_page = reverse_lazy('login')




class HomeView(ListView):
    model = CarModel
    template_name = 'home.html'
    context_object_name = 'cars'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        """
        if some one hits any brand that will triger the url in the action button and send the brand here 
        """
        brand = self.kwargs.get('brand')
        if brand :
            context['cars'] = CarModel.objects.filter(brand_id = brand)
            context['search'] = context['cars'].count()
        else:
            context['cars'] = CarModel.objects.all()
        context["brands"] =  BrandModel.objects.all()
        return context



@method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileView(ListView):
    """
    the informations of the ordercar will come here
    will be in the profile page
    they will be known as histories (date,price,car , buyer )
    """
    model = OrderCar
    template_name = 'accounts/profile.html'
    context_object_name = 'histories'

    def get_queryset(self):
        """
        filter only those informations that are related to the user who was the .

        """
        return OrderCar.objects.filter(buyer=self.request.user)
    

    def get_context_data(self, **kwargs):
        """
        get extra data about the histories 
        total price ber korte hobe
        we will extract all data from histories and will check the total price
        """
        context = super().get_context_data(**kwargs)
        for history in context['histories']:
            history.total_price = history.quantity * history.car.price
        context['total_price'] = self.request.GET.get('total_price')
        return context
