from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu
from django.core import serializers
from .models import Booking
from django.http import JsonResponse
from datetime import datetime
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


# Create your views here.


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def reservations(request):
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":booking_json})

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views
def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 

@csrf_exempt
def my_view(request):
    return HttpResponse("Hello")


def bookings(request):
    if request.method == 'GET':
        date = request.GET.get('date')
        bookings = Booking.objects.filter(reservation_date=date)
        data = [
            {
                'fields': {
                    'first_name': booking.first_name,
                    'reservation_slot': str(booking.reservation_slot),
                }
            } for booking in bookings
        ]
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        body = json.loads(request.body)
        first_name = body.get('first_name')
        reservation_date = body.get('reservation_date')
        reservation_slot = body.get('reservation_slot')

        Booking.objects.create(
            first_name=first_name,
            reservation_date=reservation_date,
            reservation_slot=reservation_slot,
        )

        return JsonResponse({'status': 'success'})

    return JsonResponse({'error': 'Invalid request method'}, status=405)