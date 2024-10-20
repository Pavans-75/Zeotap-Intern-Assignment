import requests
import time
from datetime import datetime, timezone

API_KEY = 'YOUR_OpenWeatherMap_APIKEY'  # Replace with your OpenWeatherMap API key
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
INTERVAL = 300  # Fetch data every 5 minutes

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fetch_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        main = data['weather'][0]['main']
        temp = kelvin_to_celsius(data['main']['temp'])
        feels_like = kelvin_to_celsius(data['main']['feels_like'])
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        dt = data['dt']
        dt = datetime.fromtimestamp(dt, timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        return {"city": city, "main": main, "temp": temp, "feels_like": feels_like, "humidity": humidity, "wind_speed": wind_speed, "dt": dt}
    else:
        print(f"Failed to get data for {city}: {data['message']}")
        return None

def fetch_weather_forecast(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        forecasts = []
        for forecast in data['list']:
            main = forecast['weather'][0]['main']
            temp = kelvin_to_celsius(forecast['main']['temp'])
            feels_like = kelvin_to_celsius(forecast['main']['feels_like'])
            humidity = forecast['main']['humidity']
            wind_speed = forecast['wind']['speed']
            dt = forecast['dt']
            dt = datetime.fromtimestamp(dt, timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
            forecasts.append({"city": city, "main": main, "temp": temp, "feels_like": feels_like, "humidity": humidity, "wind_speed": wind_speed, "dt": dt})
        return forecasts
    else:
        print(f"Failed to get forecast data for {city}: {data['message']}")
        return None

if __name__ == "__main__":
    for city in CITIES:
        weather_data = fetch_weather_data(city)
        print(f"Weather in {city}: {weather_data}")
        
        forecasts = fetch_weather_forecast(city)
        if forecasts:
            for forecast in forecasts:
                print(forecast)
