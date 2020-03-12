from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import permission_required
from mainshop.models import Category,Event,Ticket
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='mainshop')
@permission_required('mainshop.add_event',login_url='mainshop')
def add_event(request):
    context = {}
    if request.POST:
        event_name = request.POST.get('eventname')
        description = request.POST.get('description')
        even_date = request.POST.get('event_date')
        event_time = request.POST.get('event_time')
        location = request.POST.get('location')
        ticket_price = request.POST.get('ticket_price')
        ticket_amount = request.POST.get('ticket_amount')
        picture = request.FILES['picture']
        is_popular = request.POST.get('is_popular')
        category_id = request.POST.get('category')
        event = Event.objects.create(event_name=event_name,
            description=description,
            even_date=even_date,
            event_time=event_time,
            location=location,
            ticket_price=ticket_price,
            ticket_amount=ticket_amount,
            picture=picture,
            is_popular=is_popular,
            category_id=Category.objects.get(pk=category_id)
        )
    main_category = Category.objects.all()
    return render(request,'addevent.html',context={
        'main_category' : main_category
    })


@login_required(login_url='mainshop')
@permission_required('mainshop.delete_event',login_url='mainshop')
def manage_event(request):
    context={}
    all_event = Event.objects.all()
    return render(request,'alleventadmin.html',context={
        'all_event' : all_event
    })

@login_required(login_url='mainshop')
@permission_required('mainshop.delete_event',login_url='mainshop')
def del_event(request):
    context={}
    if request.POST:
        del_event = Event.objects.get(pk=request.POST.get('del'))
        if del_event.ticket_sold==0:
            del_event.delete()
        else:
            messages.info(request, 'ลบไม่ได้')
    all_event = Event.objects.all()
    return render(request,'alleventadmin.html',context={
        'all_event' : all_event
    })
