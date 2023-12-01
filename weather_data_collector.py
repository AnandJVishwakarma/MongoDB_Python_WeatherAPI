import requests
import json
from config import WEATHER_API_GET_DATA, WEATHER_API_GET_LAT_LONG, WEATHER_APIKEY
from common_functions import printException
from mongodb_crud import insertData

# Description: Fetch latitude and longitude based on location name from openweatherapi.
def getlatlongByLoctnName(location_name: str) -> dict:
    try:
        if location_name:
            get_latlong = WEATHER_API_GET_LAT_LONG.format(location = location_name, APIkey = WEATHER_APIKEY)
            get_latlong_response = requests.get(url=get_latlong)
            get_latlong_response = json.loads(get_latlong_response.content)
            lat, long = get_latlong_response[0]['lat'], get_latlong_response[0]['lon']
            return {'lat':lat,'long': long}
    except (Exception) as error:
        printException("getlatlongByLoctnName", error)

# Description: Fetch wether data for particular location from openweatherapi.
def getWeatherData(request: dict) -> dict:
    try:
        if 'location' in request and request['location']:
            lat, long = "",""
            latlong_data = getlatlongByLoctnName(request['location'])
            if 'lat' in latlong_data and 'long' in latlong_data:
                lat, long =  latlong_data['lat'], latlong_data['long']
            get_weather_data = WEATHER_API_GET_DATA.format(lat = lat, lon = long, part = "daily", APIkey = WEATHER_APIKEY)
            get_weather_dataresponse = requests.get(url=get_weather_data)
            get_weather_dataresponse = json.loads(get_weather_dataresponse.content)
            return {'lat':lat,'long': long, "data":get_weather_dataresponse}
    except (Exception) as error:
        printException("getWeatherData", error)

# Description: Main function.
def main():
    user_input_location = str(input("Enter the location name: "))
    weather_service = getWeatherData({
        "location":user_input_location
    })
    insertData("weather_data", {**weather_service["data"],**{"location":user_input_location}})

if __name__ == "__main__":
    main()
