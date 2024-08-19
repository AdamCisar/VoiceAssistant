import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry
import geocoder
import requests

def WeatherApi():
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    g = geocoder.ip('me')  # Uses IP address to get location
    latitude = g.latlng[0] if g.latlng else None
    longitude = g.latlng[1] if g.latlng else None

    params = {
        "latitude": 52.52,
        "longitude": 13.41,
        "hourly": "temperature_2m"
    }

    url = "https://api.open-meteo.com/v1/forecast"
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]


    # Extract current weather data
    current_weather = response.Hourly()
    breakpoint()

    # Print the current temperature and time
    print(f"Current temperature at {current_weather}°C")
WeatherApi()