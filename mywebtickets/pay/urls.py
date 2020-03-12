from django.urls import include, path
from . import views

urlpatterns = [
    path('<int:event_id>/', views.my_pay,name='my_pay')

]
