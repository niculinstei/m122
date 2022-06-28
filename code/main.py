import requests
import json
from urllib.request import urlopen

API_KEY = "6612968d9b1f2c245fed7442ad724039"


def getcity():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    city = json.load(response)['region']
    return city


url = f'https://api.openweathermap.org/data/2.5/weather?q=%7Bgetcity()%7D&appid=%7BAPI_KEY%7D&units=metric'
data = requests.get(url).json()
temp = data['main']['temp']
humidity = data['main']['humidity']

print(f'In {getcity()} beträgt die Temperatur {temp}°. Die Luftfeuchtigkeit beträgt {humidity}%.')
