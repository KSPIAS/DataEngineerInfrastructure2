import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
CITY = os.getenv("CITY")
API_URL = os.getenv("WEATHER_API_URL")

def extract_weather():
    params = {
        'access_key': API_KEY,
        'query': CITY
    }
    response = requests.get(API_URL, params=params)
    response.raise_for_status()
    return response.json()

# if __name__ == "__main__":
#     data = extract_weather()
#     print(data)
