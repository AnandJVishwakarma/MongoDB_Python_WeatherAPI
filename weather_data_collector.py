import sys
import os
import requests
import json
from mongodb_crud import insertData

# =========================================== VARIBALES : START ================================================== #
# Secret keys imports...
WEATHER_APIKEY = os.getenv('OPEN_WEATHER_API_KEY','11becd9b4f1c073ab5ea578f43d33f3a')
# External URLs...
WEATHER_API_GET_DATA     = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&exclude={part}&appid={APIkey}"
WEATHER_API_GET_LAT_LONG = "http://api.openweathermap.org/geo/1.0/direct?q={location}&appid={APIkey}"
# =========================================== VARIBALES : END ================================================== #


# =========================================== COMMON FUNCTIONS : START ================================================== #
def printException(func_name: str, error: str) -> None:
    print(f'{func_name}: {error}')
    _, __, exc_tb = sys.exc_info()
    print(f'Line No: {exc_tb.tb_lineno}')
# =========================================== COMMON FUNCTIONS : END ================================================== #


def getlatlongByLoctnName(location_name: str) -> dict:
    try:
        if location_name:
            get_latlong = WEATHER_API_GET_LAT_LONG.format(location = location_name,APIkey = WEATHER_APIKEY)
            get_latlong_response = requests.get(url=get_latlong)
            get_latlong_response = json.loads(get_latlong_response.content)
            lat, long = get_latlong_response[0]['lat'], get_latlong_response[0]['lon']
            return {'lat':lat,'long': long}
    except (Exception) as error:
        printException("getlatlongByLoctnName", error)

def getWeatherData(request: dict) -> dict:
    try:
        if 'location' in request and request['location']:
            lat, long = "",""
            latlong_data = getlatlongByLoctnName(request['location'])
            if 'lat' in latlong_data and 'long' in latlong_data:
                lat, long =  latlong_data['lat'], latlong_data['long']
            get_weather_data = WEATHER_API_GET_DATA.format(lat = lat, lon = long, part = "daily",APIkey = WEATHER_APIKEY)
            get_weather_dataresponse = requests.get(url=get_weather_data)
            get_weather_dataresponse = json.loads(get_weather_dataresponse.content)
            return {'lat':lat,'long': long, "data":get_weather_dataresponse}
    except (Exception) as error:
        printException("getWeatherData", error)


def main():
    user_input_location = str(input("ENter the location name: "))
    weather_service = getWeatherData({
        "location":user_input_location
    })
    insertData("weather_data", {**weather_service["data"],**{"location":user_input_location}})

if __name__ == "__main__":
    main()
