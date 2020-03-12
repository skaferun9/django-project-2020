
from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_event,name='add_event'),
    path('manage_event/', views.manage_event,name='alleventadmin'),
    path('manage_event/del_event', views.del_event,name='delevent')
]