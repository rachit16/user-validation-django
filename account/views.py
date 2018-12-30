from django.shortcuts import render , redirect
from django.contrib import auth
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.messages import get_messages
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm , ScRegistrationFrom
from .models import ScRegisteration
from django.contrib.auth.decorators import login_required
#...

def login(request):
    if request.user.is_authenticated:
        return redirect('admin_page')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect('admin_page')

        else:
            messages.error(request, 'Error wrong username/password')

    return render(request, 'account/login.html')


def logout(request):
    auth.logout(request)
    return render(request,'account/logout.html')


def admin_page(request):
    if not request.user.is_authenticated:
        return redirect('account_login')

    return render(request, 'account/admin_page.html')

def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password_change')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/password_change.html', {'form': form })

def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')

    else:
        f = CustomUserCreationForm

    return render(request, 'account/register.html', {'form': f})

@login_required
def sc_registration(request):
    sc_list=['a','b','c','ronish','rachit']
    sc_names = ScRegisteration.objects.all().order_by('name')
    if request.method == 'POST':
        f = ScRegistrationFrom(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'SC Name added Successfully.')
            return redirect('sc_registration')
    else:
        f = ScRegistrationFrom()
    return render(request , 'account/scregister.html' , {'form' : f , 'sc_list' : sc_list , 'sc_names' : sc_names})
