# Project 33 - Workout Tracking
"""
Build an exercise tracking app using natural language processing and Google sheets.
For this program to work, you need to add your own data as well as your API keys as environment variables first.
"""
import requests
from datetime import datetime
import os


# Your data
GENDER = "YOUR_GENDER"
WEIGHT_KG = "YOUR_WEIGHT"
HEIGHT_CM = "YOUR_HEIGHT"
AGE = "YOUR_AGE"

# ID and API Key as environment variables
APP_ID = os.environ["ENV_NIX_APP_ID"]
API_KEY = os.environ["ENV_NIX_API_KEY"]

# Nutritionix API
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
EXERCISE_TEXT = input("Tell me which exercises you did: ")

# Sheety API
SHEET_ENDPOINT = os.environ["ENV_SHEETY_ENDPOINT"]
GOOGLE_SHEET_NAME = "NAME"

TODAY = datetime.now().strftime("%d/%m/%Y")
TIME = datetime.now().strftime("%X")


# Nutritionix API Call
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": EXERCISE_TEXT,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(EXERCISE_ENDPOINT, json=parameters, headers=headers)
result = response.json()
print(f"Nutritionix API call: \n {result} \n")


# Sheety API Call
for exercise in result["exercises"]:
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {
            "date": TODAY,
            "time": TIME,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Sheety Authentication
    sheet_response = requests.post(
        SHEET_ENDPOINT,
        json=sheet_inputs,
        auth=(
            os.environ["ENV_SHEETY_USERNAME"],
            os.environ["ENV_SHEETY_PASSWORD"],
        )
    )

    print(f"Sheety Response: \n {sheet_response.text}")
