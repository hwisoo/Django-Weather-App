import os
import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

from dotenv import read_dotenv

read_dotenv('.ENV')
WEATHER_API_KEY = (os.environ.get('WEATHER_API_KEY'))

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'
    city = 'Houston'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []
    
    for city in cities:
        r = requests.get(url.format(city, WEATHER_API_KEY)).json()

        city_weather = {
          'city': city.name.title(),
          'temperature': r['main']['temp'],
          'description': r['weather'][0]['description'].title(),
          'icon': r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)


    context = {'weather_data' : weather_data, 'form': form}
    return render(request, 'weather/weather.html', context)