from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from .forms import LoginForm
from django.contrib import messages, auth





def login(request):
    """Users will be authenticated through this form and redirected to cookies.html"""
    if request.method=='POST':
        user_form=LoginForm(request.POST)
        if user_form.is_valid():
            user=auth.authenticate(request.POST['username'],
                    password=request.POST['password'])
                    
            if user:
                auth.login(request, user)
                
                return redirect(reverse('allcookies'))
    else:
        user_form=LoginForm()
        
    args={'user_form':user_form}
    return render(request, 'login.html', args)