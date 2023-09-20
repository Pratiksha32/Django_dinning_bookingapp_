from django.shortcuts import render, redirect
from .models import Booking

# Create your views here.

def indexview(request):
    return render(request, 'bookingapp\index.html')

def roomsview(request):
    return render(request, 'bookingapp/rooms.html')

def dinningview(request):
    return render(request, 'bookingapp/dinning.html')
 
def galleryview(request):
    return render(request, 'bookingapp/gallery.html')

def menuview(request):
    return render(request, 'bookingapp/menu.html')

def contactview(request):
    return render(request, 'bookingapp/contact.html')

def bookview(request):

    if request.method =='POST':
        print(request.POST)
        
        u_nm = request.POST.get('name')
        u_mobile = int(request.POST.get('mobile'))
        u_checkin = request.POST.get('checkin')
        u_checkout = request.POST.get('checkout')
        u_roomtype = request.POST.get('roomtype')
        
        b1 = Booking(name = u_nm, mobile = u_mobile, checkin =u_checkin, checkout = u_checkout, roomtype= u_roomtype)
        b1.save()

        return redirect("/bookingapp/display/")



    return render(request, 'bookingapp/booking.html')


def displayview(request):
    data = Booking.objects.all()

    context ={ 'data': data}

    return render(request, 'bookingapp/display.html', context) 

def updateview(request,id):
    data = Booking.objects.get(pk = id)
    print(data)
    context ={ 'data': data 
              }
    
    if request.method == 'POST':
        data = Booking.objects.get(pk = id)
        u_nm = request.POST.get('name')
        u_mobile = int(request.POST.get('mobile'))
        u_checkin = request.POST.get('checkin')
        u_checkout = request.POST.get('checkout')
        u_roomtype = request.POST.get('roomtype')

        data.name = u_nm
        data.mobile = u_mobile
        data.checkin = u_checkin
        data.checkout = u_checkout
        data.roomtype = u_roomtype
        data.save()

        return redirect("/bookingapp/display/")

    return render(request, 'bookingapp/update.html', context) 
    
def deleteview(request,id):
    data = Booking.objects.get(pk = id)
    data.delete()
    return redirect("/bookingapp/display/")





