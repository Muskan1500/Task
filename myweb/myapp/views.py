# myapp/views.py
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm

def home(request):
    return render(request, 'home.html')

def signup(request):
    print(request.method)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print("sdghskj")
        if form.is_valid():
            print("abcd")
            user = form.save()
            login(request, user)
            messages.success(request, 'Signup successful!')
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')  # Replace 'home' with the name of your home view
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')  # Replace 'home' with the name of your home view

def contact(request):
    if request.method == 'POST':
        # Handle contact form submission and save to database
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        ContactSubmission.objects.create(name=name, email=email, message=message)

        messages.success(request, 'Your message has been submitted!')
        return redirect('home')
    return render(request, 'contact.html')





# Create your views here.
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .models import UserProfile, ContactSubmission

# def home(request):
#     return render(request, 'home.html')

# def login(request):
#     if request.method == 'POST':
#         # Handle login logic here (authentication)
#         messages.success(request, 'Login successful!')
#         return redirect('home')
#     return render(request, 'login.html')

