from django.shortcuts import render, redirect
from user.forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from client.models import Client


# Create your views here.
def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            Client.objects.create(user=user)
            login(request, user)

            return redirect('client:client_contact_page')
    else:
        form = SignupForm()
    return render(request, "auth-form.html", {
        "form":form,
        "header":"Start Your Job Searching Journey With Us",
        "form_type": "signup",
        })

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,  username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = LoginForm(request)
    return render(request, "auth-form.html", {
        "form":form,
        "header":"Welcome back..",
        "form_type": "login",
        })

def logout_view(request):
    logout(request)
    
    return redirect('user:login')