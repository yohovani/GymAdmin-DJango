from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import requests

# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email,password=password)
        
        if user is not None:
            auth.login(request, user)
            url = request.META.get('HTTP_REFERER')
            try:
                query = requests.utils.urlparse(url).query
                params = dict(x.split('=') for x in query.split('&'))
                if 'next' in params:
                    nextPage = params['next']
                    return redirect(nextPage)
                else:
                    return redirect('dashboard')
            except:
                return redirect('dashboard')
    
    return render(request,'accounts/login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')