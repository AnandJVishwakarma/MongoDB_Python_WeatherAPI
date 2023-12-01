import os
import sys

# Secret keys imports...
WEATHER_APIKEY = os.getenv('OPEN_WEATHER_API_KEY','')
# External URLs...
WEATHER_API_GET_DATA     = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&exclude={part}&appid={APIkey}"
WEATHER_API_GET_LAT_LONG = "http://api.openweathermap.org/geo/1.0/direct?q={location}&appid={APIkey}"
# MongoDB configurations...
DATABASE_HOST = os.getenv('DATABASE_HOST','mongodb://localhost:27018/')
DATABASE_NAME = os.getenv('DATABASE_NAME','WeatherData')
