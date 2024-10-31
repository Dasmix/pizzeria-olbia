from django.shortcuts import render
from django.views import generic
from .models import Reservation
# Create your views here.


class HomeView(generic.ListView):
    model = Reservation
    template_name = 'booking/index.html'

def register(request):
    return render(request, 'booking/register.html')

def book_table(request):
    return render(request, 'booking/book_table.html')

def manage_reservation(request):
    return render(request, 'booking/manage_reservation.html')