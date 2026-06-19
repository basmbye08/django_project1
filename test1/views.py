
#from django.http import HttpResponse

from django.shortcuts import render, HttpResponse, redirect
from .models import Product, ContactMessage
from .forms import ContactForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User




# Create your views here.

def loginuser(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "invalid email or password!")
    else:
        form = AuthenticationForm(request)

    if request.GET.get('next'):
        messages.warning(request, "Please log in to view products.")

    for field in form.fields.values():
        field.widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})

    return render(request, "test1/loginuser.html", {'form': form})


def signupuser(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        username = request.POST.get('username', '').strip()
        first_name = request.POST.get('first_name', '').strip()
        if username and User.objects.filter(username__iexact=username).exists():
            form.add_error('username', 'This username is already taken. Please choose another.')

        if form.is_valid():
            user = form.save()
            if first_name:
                user.first_name = first_name
                user.save()
            login(request, user)
            messages.success(request, 'Your account has been created successfully.')
            return redirect('home')
    else:
        form = UserCreationForm()

    for field in form.fields.values():
        field.widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})

    return render(request, "test1/signupuser.html", {'form': form})

def logoutuser(request):
    if request.method == "GET":
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
        return redirect('home')


def findproduct(request):
    search_term = request.GET.get('prod_search', '').strip()
    if search_term:
        product_info = Product.objects.filter(
            Q(product_name__icontains=search_term) |
            Q(product_description__icontains=search_term) |
            Q(product_category__icontains=search_term)
        ).distinct()
        if not product_info.exists():
            messages.info(request, f'No products matched "{search_term}".')
    else:
        product_info = Product.objects.all()

    return render(request, "test1/home.html", {"product_info": product_info})


@login_required(login_url='loginuser')
def product(request):
    my_product = Product.objects.all()
    paginator = Paginator(my_product, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "test1/product.html", {"page_obj": page_obj})


def home(request):
    product_info = Product.objects.all()
    return render(request, "test1/home.html", {"product_info": product_info})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your message has been sent successfully. We will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, "test1/contact.html", {'form': form})

@login_required(login_url='loginuser')
def product(request):
    my_product = Product.objects.all()
    paginator = Paginator(my_product, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "test1/product.html", {"page_obj": page_obj})

def about(request):
    return render(request, 'test1/about.html')

