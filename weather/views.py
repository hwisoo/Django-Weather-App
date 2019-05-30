import os
import requests
from dotenv import read_dotenv
from django.shortcuts import render

read_dotenv('.ENV')
WEATHER_API_KEY = (os.environ.get('WEATHER_API_KEY'))

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'
    city = 'Seattle'
    r = requests.get(url.format(city, WEATHER_API_KEY))
    print(r.text)

    
    return render(request, 'weather/weather.html')