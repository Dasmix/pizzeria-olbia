from django.shortcuts import render
from django.views import generic
from .models import Reservation
# Create your views here.


class HomeView(generic.ListView):
    model = Reservation
    template_name = 'booking/index.html'