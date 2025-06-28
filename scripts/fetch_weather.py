import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("WEATHER_API_URL")
ACCESS_KEY = os.getenv("WEATHER_API_KEY")
DEFAULT_LOCATION = os.getenv("CITY")

def fetch_weather_data(location: str = DEFAULT_LOCATION) -> dict:
    params = {
        "access_key": ACCESS_KEY,
        "query": location,
    }
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if "location" in data and "current" in data:
            return data
        else:
            raise ValueError("Missing expected keys in API response")
    else:
        raise ConnectionError(f"API request failed with status {response.status_code}")
