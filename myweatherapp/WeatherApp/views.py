from datetime import datetime
import json
import requests   #pipenv install requets
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages
from .models import City
from .forms import CityForm
import urllib.request
from IPython.display import Image, display

def home(request):
    if 'term' in request.GET:
        cities = City.objects.filter(name__istartswith=request.GET.get("term"))
        list1=[]
        for c in cities:
            list1.append(c.name)
        return JsonResponse(list1,safe=False)
    if 'location' in request.GET:
        city = request.GET.get('location')
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=ce1634780a3a782d1f36fbab201bce67&units=metric"
        x = requests.get(url)
        y = x.json()
        context = {
            'c_name' : f"City_name:{y['name']}",
            'icon': y['weather'][0]['icon'],
            'country_code':f"country_code:{str(y['sys']['country'])}",
            'Temperature': f"Temperature: {str(y['main']['temp'])}  °C",
            'Pressure': f"Pressure: {str(y['main']['pressure'])}",
            'Humidity': f"Humidity: {y['main']['humidity']}",
            'Weather_condition': f"Weather_Condition: {y['weather'][0]['description'].upper()}"
    
        }

        return render(request, 'weatherapp.html', context)
    return render(request, 'weatherapp.html')
    
# using urlib api
    #  if request.method == 'POST':
    #     city = request.POST['city']
    #     # source contain JSON data from API
    #     source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=ce1634780a3a782d1f36fbab201bce67').read()
    #     current_time = datetime.now()
    #     formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p")
    #     # converting JSON data to a dictionary
    #     list_of_data = json.loads(source)

    #     # data for variable list_of_data
    #     data = {
    #         'city': city,
    #         'icon': list_of_data['weather'][0]['icon'],
    #         "country_code": str(list_of_data['sys']['country']),
    #         "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
    #         "temp": str(list_of_data['main']['temp']) + 'k',
    #         "pressure": str(list_of_data['main']['pressure']),
    #         "humidity": str(list_of_data['main']['humidity']),
    #         'time': formatted_time
    #     }
    #     print(data)
    #  else:
    #     data ={}
    #  return render(request, "weatherapp.html", data)

# using request api
    # url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=ce1634780a3a782d1f36fbab201bce67'
    # cities = City.objects.all()
    # # city = 'Las Vegas'
    # # city_weather = requests.get(url.format(city)).json()
    # if request.method == 'POST':  # only true if form is submitted
    #     form = CityForm(request.POST)  # add actual request data to form for processing
    #     form.save()  # will validate and save if validate
    # form = CityForm()
    # weather_data = []
    # for city in cities:
    #     response = requests.get(url.format(city))
    #     if response.status_code == 404:
    #         continue
    #     city_weather = response.json()
    #     current_time = datetime.now()
    #     formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p")
    #     weather = {

    #         'city': city,
    #         'description': city_weather['weather'][0]['description'],
    #         'icon': city_weather['weather'][0]['icon'],
    #         'temperature': 'Temperature: ' + str(city_weather['main']['temp']) + ' °C',
    #         'country_code': city_weather['sys']['country'],
    #         'wind': 'Wind: ' + str(city_weather['wind']['speed']) + 'km/h',
    #         'humidity': 'Humidity: ' + str(city_weather['main']['humidity']) + '%',
    #         'time': formatted_time
    # }
    # weather_data.append(weather)
    # context = {'weather_data' : weather_data, 'form' : form}
    # return render(request, "weatherapp.html", context)
   


    
      
                   
                
          

              
