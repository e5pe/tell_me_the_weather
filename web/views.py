from django.shortcuts import render
from decouple import config
import requests

from .forms import SearchForm

API_KEY = config('API_KEY')


def index(request):
    code = None  # If code == None or 200 everything gone well
    message = None
    city_weather = {}

    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            temperatureUnits = 'c'
            # by default for now is gonna be in celsius
            units = getTemperature(temperatureUnits.lower())
            url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid={}'
            city = form.cleaned_data['search']
            # Para no gastar tantas llamadas a la api y arreglar la vista lo dejamos comentado
            r = requests.get(url.format(city, units, API_KEY)).json()
            # r = {'coord': {'lon': -0.48, 'lat': 38.35}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}], 'base': 'stations', 'main': {'temp': 20.18, 'feels_like': 16.19, 'temp_min': 18.89, 'temp_max': 22.78, 'pressure': 1020, 'humidity': 37},'visibility': 10000, 'wind': {'speed': 4.1, 'deg': 100}, 'clouds': {'all': 39}, 'dt': 1582901422, 'sys': {'type': 1, 'id': 6391, 'country': 'ES', 'sunrise': 1582871792, 'sunset': 1582912379}, 'timezone': 3600, 'id': 2521978, 'name': 'Alicante', 'cod': 200}
            # r = {'cod': '404', 'message': 'city not found'}
            code = r['cod']
            if r['cod'] == 200:
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
            # if the request goes wrong we show an error message
            elif r['cod'] == '404':
                message = '{}, {}'.format(city, r['message'])
                print(message)
    else:
        form = SearchForm()
    context = {'city_weather': city_weather,
               'form': form, 'code': code, 'message': message}
    return render(request, 'weather/current_weather.html', context)


def getTemperature(units):
    temperature = ''  # by default the API uses Kelvin
    if units == 'c':
        temperature = 'metric'
    elif units == 'f':
        temperature = 'imperial'
    return temperature
