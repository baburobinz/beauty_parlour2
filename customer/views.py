from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import UserDetails
from django.http import JsonResponse

# Create your views here.


def user_registraion_and_login(request):

    if request.POST and 'register' in request.POST:

        user_name = request.POST.get('username')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        try:
            user = User.objects.create_user(
                username=user_name,
                password=password)
            user_detail = UserDetails.objects.create(
                user=user,
                mobile=mobile
            )
            user_detail.save()

            return JsonResponse({'success':'Registration Successful'})
        
        except Exception as e:

             return JsonResponse({'error':'Username Already Exist'})
        
        
    elif request.POST and 'login' in request.POST:
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=user_name,password=password)

        if user is not None:
            login(request,user)

            if user.is_superuser:
                print('super user')

                return JsonResponse({'url':'admin'})

            else:
                print('not super')
                return JsonResponse({'url':''})

        
        return JsonResponse({'error':'Invalid Username or Password'})


def user_logout(request):

    logout(request)
    return redirect('show_home')