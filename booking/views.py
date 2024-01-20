from django.shortcuts import render

# Create your views here.
def show_bookings(request):

    return render(request,'my_bookings.html')