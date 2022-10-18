from django.contrib import messages,auth    
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from accounts.models import Account
from .forms import RegistrationForm
# Create your views here.

def register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name  = form.cleaned_data['last_name']
            phone      = form.cleaned_data['phone']
            email      = form.cleaned_data['email']
            password   = form.cleaned_data['password']
            username   = email.split('@')[0]

            user =  Account.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
            user.phone=phone
            user.save()
            messages.success(request,'Registration successful.')
            return redirect('register')
    else:
        form = RegistrationForm()

    
    context = {
        'form':form,
    }
    return render(request,'accounts/register.html',context)

def login(request):
    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email,password=password)

        if user is not None:
            auth.login(request,user)
            # messages.success(request,'You are now logged in.')
            return redirect('home')
        else:
            messages.error(request,'Invalid login credentials')
            return redirect('login')

    return render(request,'accounts/login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request,'You are  loggedd out.')
    return redirect('login')