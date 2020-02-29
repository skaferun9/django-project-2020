from django.urls import include, path
from . import views

urlpatterns = [
    path('<int:event_id>/<int:count>', views.my_pay,name='my_pay')

]
