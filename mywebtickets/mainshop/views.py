


from django.http import HttpResponse
from django.shortcuts import render
from mainshop.models import Category, Event


def mainshop(request):
    is_pop = Event.objects.filter(is_popular=True)
    main_category = Category.objects.all()
    return render(request,'mainshop.html',context={
        'popevent' : is_pop,
        'main_category' : main_category
    })

def my_detail(request,event_id):
    event = Event.objects.get(pk=event_id)
    return render(request,'detail.html',context={
        'eventinfo' : event
    })


# Create your views here.
