from django.shortcuts import render
from decouple import config
import requests

API_KEY = config('API_KEY')

def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    city = 'Alicante'
    r = requests.get(url.format(city,API_KEY)).json()
    print(r.text)

    # city_weather = {
    #     ''
    # }
    return render(request, 'weather/index.html')