from django.urls import path
from . import views
app_name='lpapp'

urlpatterns = [
   path('',views.service,name='service'),
]