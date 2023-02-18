
from django.shortcuts import render, redirect
from .forms import UserForm, ProductForm, ReviewForm
from .models import Product, User, Review

def product_list(request):
    products = Product.objects.all()
    return render(request, 'layout/views/product_list.html', {'products': products})

def user_list(request):
    users = User.objects.all()
    return render(request, 'layout/views/users_list.html', {'users': users})

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'layout/views/review_list.html', {'reviews': reviews})

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            form = UserForm()
    else:
        form = UserForm()
    return render(request, 'layout/forms/users.html', {'form': form})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProductForm()
    else:
        form = ProductForm()
    return render(request, 'layout/forms/products.html', {'form': form})
     
def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            form = ReviewForm()
    else:
        form = ReviewForm()
    return render(request, 'layout/forms/reviews.html', {'form': form})