
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


def my_signup(request):
    if request.POST:
        username = request.POST.get('signupusername')
        email = request.POST.get('signupemail')
        password = request.POST.get('signuppassword')
        firstname = request.POST.get('signupfirstname')
        lastname = request.POST.get('signuplastname')
        user = User.objects.create_user(username=username, 
            email=email, 
            password=password,
            first_name=firstname,
            last_name=lastname)
        return redirect('mainshop')
    return render(request,'signup.html')
