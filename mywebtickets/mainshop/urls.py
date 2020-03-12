from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.mainshop,name='mainshop'),
    path('detail/<int:event_id>',views.my_detail,name='my_detail'),
    path('alleventbycat/<int:category_id>',views.allbycat,name='allbycat'),
    path('allevent',views.allevent,name='allevent'),
    path('search',views.search,name='search'),
    path('hisevent',views.his_event,name='hisevent')
]
