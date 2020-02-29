from django.http import HttpResponse
from django.shortcuts import render



def my_pay(request,event_id,count):
    return HttpResponse('test')
