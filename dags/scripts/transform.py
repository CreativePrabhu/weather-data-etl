import json
import os

# Set the base directory relative to this file's location
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
# Use absolute path to access the data folder
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Modify file paths accordingly
RAW_PATH = os.path.join(DATA_DIR, 'raw_weather.json')
CLEAN_PATH = os.path.join(DATA_DIR, 'clean_weather.json')

def transform_weather():
    # Read the raw weather JSON from the file
    with open(RAW_PATH, "r") as f:
        data = json.load(f)

    # Extract relevant fields and clean the data
    cleaned_data = {
        "city": data.get("name"),
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["description"],
        "wind_speed": data["wind"]["speed"]
    }

    # Save the cleaned data to a new file
    with open(CLEAN_PATH, "w") as f:
        json.dump(cleaned_data, f)

    print("✅ Weather data transformed and saved.")
