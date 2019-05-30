import os
import requests
from dotenv import read_dotenv
from django.shortcuts import render

read_dotenv('.ENV')
WEATHER_API_KEY = (os.environ.get('WEATHER_API_KEY'))

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'
    city = 'Houston'
    r = requests.get(url.format(city, WEATHER_API_KEY)).json()

    city_weather = {
      'city': city,
      'temperature': r['main']['temp'],
      'description': r['weather'][0]['description'],
      'icon': r['weather'][0]['icon'],
    }

    context = {'city_weather' : city_weather}
    return render(request, 'weather/weather.html', context)