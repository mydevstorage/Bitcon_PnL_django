from .views import *
from django.urls import path


app_name= 'pnl_index'

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
]
