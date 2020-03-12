from django.http import HttpResponse
from django.shortcuts import render, redirect
from mainshop.models import Ticket, Event,User
import datetime
from django.contrib.auth.decorators import login_required

def my_pay(request,event_id):
    userr = {}
    if request.user.is_authenticated:
        userr = User.objects.get(username=request.user)
    event = Event.objects.get(id=event_id)
    total = 0
    if request.method == 'GET':
        ticket = request.GET.get('ticket')
        total = int(ticket)*event.ticket_price
    now_date = datetime.date.today()
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('first_name')
        email = request.POST.get('first_name')
        ticket = request.POST.get('ticket')
        if request.user.is_authenticated:
            for i in range(int(ticket)):
                Ticket.objects.create(owner_id=request.user,event_id=event)
                ticket_count = event.ticket_set.all().count()
                event.ticket_sold = ticket_count
                event.save()
            return redirect('mainshop')
        else:
            password = request.POST.get('password')
            username = request.POST.get('username')
            email = request.POST.get('email')
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            user = User.objects.create_user(username=username, 
            email=email, 
            password=password,
            first_name=firstname,
            last_name=lastname)
            # สร้าง user
            for i in range(int(ticket)):
                Ticket.objects.create(owner_id=user,event_id=event)
                ticket_count = event.ticket_set.all().count()
                event.ticket_sold = ticket_count
                event.save()
            return redirect('mainshop')
    return render(request,'paypage.html',context={
        'pay_event':event,
        'date':now_date,
        'ticket':int(ticket),
        'total':total,
        'userr':userr
        })
