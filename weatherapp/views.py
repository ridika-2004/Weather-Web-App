from django.shortcuts import render
import requests
import datetime

# Create your views here.
from django.shortcuts import render
import requests
import datetime

def home(request):
    description = icon = temp = city = None

    if request.method == 'POST':
        city = request.POST.get('city', '').strip()
        if city:  # only make request if city is provided
            url = 'https://api.openweathermap.org/data/2.5/weather'
            PARAMS = {
                'q': city,
                'appid': '68a8d20019709116188e3b47090fe0a5',
                'units': 'metric'
            }

            response = requests.get(url, params=PARAMS)
            data = response.json()

            if data.get('cod') == 200:
                description = data['weather'][0]['description']
                icon = data['weather'][0]['icon']
                temp = data['main']['temp']
            else:
                city = None  # clear city if not found

    day = datetime.date.today()

    return render(request, 'weatherapp/index.html', {
        'description': description,
        'icon': icon,
        'temp': temp,
        'day': day,
        'city': city
    })
