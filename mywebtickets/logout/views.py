
import json
from django.contrib.auth import authenticate, login, logout
from django.db.models import Count
from django.forms import formset_factory
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='mainshop')
def my_logout(request):
    logout(request)
    return redirect('login')
