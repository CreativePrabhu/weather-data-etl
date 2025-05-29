import json
import csv
import os
from datetime import datetime

# Set the base directory relative to this file's location
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
# Use absolute path to access the data folder
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Modify file paths accordingly
INPUT_FILE = os.path.join(DATA_DIR, 'clean_weather.json')
OUTPUT_FILE = os.path.join(DATA_DIR, 'weather_data.csv')

def load_weather():
    # Load the clean weather data from the JSON file
    with open(INPUT_FILE, "r") as f:
        data = json.load(f)

    # Add timestamp to the data
    data["timestamp"] = datetime.now().isoformat()

    # Check if the CSV file already exists
    file_exists = os.path.isfile(OUTPUT_FILE)

    # Write the data to the CSV file
    with open(OUTPUT_FILE, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

    print("✅ Weather data loaded to CSV.")
