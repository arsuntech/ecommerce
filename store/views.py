from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms


categories = Category.objects.all()
# Create your views here.
def category(request, foo):
    foo = foo.replace('-', ' ')
    try:
        category = Category.objects.get(name = foo)
        products = Product.objects.filter(category = category)
        return render(request, 'category.html', {'products': products, 'category': category, 'categories': categories})
    except:
        messages.success(request, ('That Category Doesn`t Exist...'))
        return redirect('home')


def product(request, pk):
    product = Product.objects.get(id = pk)
    return render(request, 'product.html', {'product': product, 'categories': categories})


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products, 'categories': categories})

def about(request):
    return render(request, 'about.html', {'categories': categories})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been Login'))
            return redirect('home')
        else:
            messages.success(request, ('Something went wrong while trying to login please try again.'))
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ('You have been Logged out...Thanks for stopping by...'))
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        print('debug: 0')
        form = SignUpForm(request.POST)
        print(f'debug: 00 {form.is_valid()}')
        if form.is_valid():
            print('debug: 1')
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            print('debug: 2')
            #login user
            user = authenticate(username = username, password = password)
            print('debug: 3')
            login(request, user)
            print('debug: 4')
            messages.success(request, ('You Have Registered successfilly!!'))
            return redirect('home')
        else:
            messages.success(request, ('Something went wrong while registering please try again!!'))
            return redirect('register')
    else:
        print('debug: 5')
        return render(request, 'register.html', {'form': form})
