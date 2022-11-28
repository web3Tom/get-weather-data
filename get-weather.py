#ask user the city or town
#returns the user the details of the weather in that location
# api-location: https://home.openweathermap.org/api_keys
# api-key: 6f0a2669a64715f6d917ee4785ebc772
from pprint import pprint

import requests

API_KEY = '6f0a2669a64715f6d917ee4785ebc772'

city = input("Enter a city: ")

base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+API_KEY+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)
