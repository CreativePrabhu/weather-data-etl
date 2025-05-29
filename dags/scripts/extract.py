import requests
import os
import json

# Set the base directory relative to this file's location
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
# Use absolute path to access the data folder
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Modify file paths accordingly
RAW_PATH = os.path.join(DATA_DIR, 'raw_weather.json')
CLEAN_PATH = os.path.join(DATA_DIR, 'clean_weather.json')


def extract_weather():
    api_key = os.getenv("OPENWEATHER_API_KEY")
    city = os.getenv("WEATHER_CITY", "Berlin")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Save raw data temporarily for the next step
        with open(RAW_PATH, "w") as f:  # Use the absolute path defined above
            json.dump(data, f)
        print("✅ Weather data extracted successfully.")
    else:
        raise Exception(f"❌ Failed to fetch data: {response.status_code}, {response.text}")
