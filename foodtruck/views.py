from django.shortcuts import render
from .models import Foodtruck, Booth
from .forms import FoodtruckForm, BoothForm
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
import logging

# 푸드트럭 views.py
def foodtruck(request):
    foodtrucks = Foodtruck.objects.all()
    foodtrucks1 = foodtrucks[:int(len(foodtrucks)/2+1)]
    foodtrucks2 = foodtrucks[int(len(foodtrucks)/2+1):]
    # print(foodtrucks.name)
    return render(request,'foodtruck.html',{'foodtrucks1': foodtrucks1, 'foodtrucks2': foodtrucks2})

def haminseop(request):
    foodtrucks = Foodtruck.objects.all()
    booths = Booth.objects.all()
    # print(foodtrucks.name)
    return render(request,'haminseop.html',{'foodtrucks': foodtrucks, 'booths': booths})

def mirae(request):
    booths = Booth.objects.all()
    booths1 = booths[:int(len(booths)/2+1)]
    booths2 = booths[int(len(booths)/2+1):]
    # print(foodtrucks.name)
    return render(request,'mirae.html',{'booths1': booths1, 'booths2': booths2})

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is None:
            messages.error(request, '아이디 혹은 패스워드가 다릅니다.')
            return redirect('foodtruck:login')
        else:
            try:
                foodtruck = Foodtruck.objects.get(user=user)
                return redirect('foodtruck:foodtruck_update', pk=foodtruck.id)
            except:
                booth = Booth.objects.get(user=user)
                return redirect('foodtruck:booth_update', pk=booth.id)

def foodtruck_update(request, pk):
    foodtruck = Foodtruck.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request,'updateFoodtruck.html',{'foodtruck': foodtruck})
    else:
        form = FoodtruckForm(request.POST, request.FILES, instance=foodtruck)
        if form.is_valid():
            form.save()
            return redirect('foodtruck:foodtruck_update', pk=foodtruck.id)

def booth_update(request, pk):
    booth = Booth.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request,'updateBooth.html',{'booth': booth})
    else:
        form = BoothForm(request.POST, request.FILES, instance=booth)
        if form.is_valid():
            form.save()
            return redirect('foodtruck:booth_update', pk=booth.id)
        else:
            logging.error(form.errors)

