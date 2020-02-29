from django.shortcuts import render
from decouple import config
import requests

API_KEY = config('API_KEY')

def index(request):
    if request.method == 'POST':
        peticion = request.POST
        print(peticion)

    temperatureUnits = 'c'
    units=getTemperature(temperatureUnits.lower()) # by default now is gonna be in celsius
    # url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid={}'
    city = 'Alicante'
    # r = requests.get(url.format(city,units,API_KEY)).json()
    # Para no gastar tantas llamadas a la api y arreglar la vista
    r = {'coord': {'lon': -0.48, 'lat': 38.35}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}], 'base': 'stations', 'main': {'temp': 20.18, 'feels_like': 16.19, 'temp_min': 18.89, 'temp_max': 22.78, 'pressure': 1020, 'humidity': 37}, 'visibility': 10000, 'wind': {'speed': 4.1, 'deg': 100}, 'clouds': {'all': 39}, 'dt': 1582901422, 'sys': {'type': 1, 'id': 6391, 'country': 'ES', 'sunrise': 1582871792, 'sunset': 1582912379}, 'timezone': 3600, 'id': 2521978, 'name': 'Alicante', 'cod': 200}
    print(r)
    city_weather = {
        "city": r['name'],
        "description": r['weather'][0]['description'],
        "icon": r['weather'][0]['icon'],
        "temperature": r['main']['temp'],
        "humidity": r['main']['humidity'],
        "wind": {
            "speed": r['wind']['speed'],
            "deg": r['wind']['deg'],
        },
        "units": temperatureUnits.upper()
    }
    context = { 'city_weather': city_weather}
    return render(request, 'weather/index.html', context)

def getTemperature(units):
    temperature = '' # by default the API uses Kelvin
    if units == 'c':
        temperature = 'metric'
    elif units == 'f':
        temperature = 'imperial'
    return temperature