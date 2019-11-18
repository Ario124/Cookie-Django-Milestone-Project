from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from .forms import LoginForm, RegisterForm
from django.contrib import messages, auth
from django.template.context_processors import csrf


def login(request):
    """Users will be authenticated through this form and redirected to cookies.html"""
    if request.method=='POST':
        user_form=LoginForm(request.POST)
        if user_form.is_valid():
            user=auth.authenticate(request.POST['username'],
                    password=request.POST['password'])
                    
            if user:
                auth.login(request, user)
                messages.success(request, "You have logged in.")
                
                return redirect(reverse('allcookies'))
    else:
        user_form=LoginForm()
        
    args={'user_form':user_form}
    return render(request, 'login.html', args)
    

def registration(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            
            user = auth.authenticate(request.POST.get('email'), password=request.POST.get('password1'))
            
            if user:
                messages.success(request, "Your registration was successfully completed. You may now login.")
                return redirect(reverse('login'))
            
            else:
                messages.error(request, "This email is already in use, pick a new one.")
    else:
        user_form = RegisterForm()
        
    args = {'user_form': user_form}
    return render(request, 'register.html', args)
    
    
def logout(request):
    auth.logout(request)
    messages.success(request, "You have logged out.")
    return redirect(reverse('index'))
    