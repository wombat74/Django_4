from sqlite3 import IntegrityError
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect
from django.db import IntegrityError
from .forms import UserCreateForm

def signupaccount(request):
    if request.method == 'GET':
        return render(request, 'signupaccount.html', {'form':UserCreateForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signupaccount.html', {'form':UserCreateForm,
                                                              'error':'Username already taken. Choose new username.'})
        else:
            return render(request, 'signupaccount.html', {'form':UserCreateForm, 
                                                          'error':'Passwords do not match!'})

