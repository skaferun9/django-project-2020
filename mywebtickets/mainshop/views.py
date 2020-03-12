


from django.http import HttpResponse
from django.shortcuts import render,redirect
from mainshop.models import Category, Event,User,Ticket
from django.utils.timezone import now
from django.db.models import Q
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required


def mainshop(request):
    is_pop = Event.objects.filter(is_popular=True)
    main_category = Category.objects.all()
    return render(request,'mainshop.html',context={
        'popevent' : is_pop,
        'main_category' : main_category
    })

def my_detail(request,event_id):
    event = Event.objects.get(pk=event_id)
    ticket_count = event.ticket_set.all().count()
    event.ticket_sold = ticket_count
    event.save()
    left = event.ticket_amount - ticket_count
    return render(request,'detail.html',context={
        'eventinfo' : event,
        'range' : range(1, left + 1)
    })

def allbycat(request,category_id):
    event_category = Event.objects.filter(category_id__id=category_id)
    category = Category.objects.get(id=category_id)
    return render(request,'allbycategory.html',context={
        'event_category':event_category,
        'category':category
    })

def allevent(request):
    all_event = Event.objects.all()
    return render(request,'allevent.html',context={
        'all_event':all_event
    })

def search(request):
    if request.POST:
        text = request.POST.get('searchname')
        search_ob = Event.objects.filter(
            Q(event_name__startswith=text)|Q(category_id__category_name__startswith=text)
        )
        print(search_ob)
    return render(request,'search.html',context={
        'search_ob':search_ob
    })


@login_required(login_url='mainshop')
def his_event(request):
    userr = User.objects.get(username=request.user)
    histic = Ticket.objects.filter(owner_id__username=userr.username)
    return render(request,'histicket.html',context={
        'histic':histic
    })

# Create your views here.
