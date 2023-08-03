from django.shortcuts import render, redirect
from booking.models import Room
def home(request):
    roomData=Room.objects.all()

    data={'roomData':roomData}

    return render(request, 'index.html',data)