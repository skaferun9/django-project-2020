from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.mainshop,name='mainshop'),
    path('detail/<int:event_id>',views.my_detail,name='my_detail')
    
]
