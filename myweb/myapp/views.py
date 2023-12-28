
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfile, ContactSubmission

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        # Handle login logic here (authentication)
        messages.success(request, 'Login successful!')
        return redirect('home')
    return render(request, 'login.html')

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
