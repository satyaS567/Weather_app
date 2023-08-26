from django.shortcuts import render
import requests
import datetime
# Create your views here.

def index(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city ='noida'
    API_KEY =''#paste your api key here   
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url).json()

    temp = response['main']['temp']
    desc = response['weather'][0]['description']
    pressure = response['main']['pressure']
    icon = response['weather'][0]['icon']
    humidity = response['main']['humidity']
    wind_speed = response['wind']['speed']
    day = datetime.date.today()
    context={
        'city':city,
        'day':day,
        'temp':temp,
        'desc':desc,
        'pressure':pressure,
        'icon':icon,
        'humidity':humidity,
        'wind_speed':wind_speed
    }   
    return render(request,'index.html',context)