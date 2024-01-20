from django.shortcuts import render

# Create your views here.

def show_home(request):
    return render(request,'index.html')

def show_services(request):
    return render(request,'service.html')

def show_pricing(request):
    return render(request,'price.html')

def show_offer(request):
    return render(request,'today_offer.html')