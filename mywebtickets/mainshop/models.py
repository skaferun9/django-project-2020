
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    def __str__(self):
        return 'Category : '+self.category_name


class Event(models.Model):
    event_name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    even_date = models.DateField(null=True)
    event_time = models.TimeField(auto_now=False,auto_now_add=False)
    location = models.CharField(max_length=200,null=False)
    ticket_price = models.FloatField(null=True, blank=True, default=None)
    ticket_amount = models.IntegerField(null=True, blank=True, default=None)
    picture = models.ImageField(default='')
    is_popular = models.BooleanField(null=True)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    ticket_sold = models.IntegerField(null=True,default=0)
    def __str__(self):
        return 'Event : '+self.event_name


class Ticket(models.Model):
    event_id = models.ForeignKey(Event,on_delete=models.CASCADE)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    purchased_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return 'Ticket no : '+str(self.id) +'  ' +self.event_id.event_name
