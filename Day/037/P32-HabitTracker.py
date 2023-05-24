# Project 32 - Habit Tracker
"""
This program tracks your habits.

For more information:
https://pixe.la
"""
import requests
from datetime import datetime


USERNAME = "YOUR_USERNAME"  # Create your own
TOKEN = "YOUR_TOKEN"  # Create your own
HEADERS = {"X-USER-TOKEN": TOKEN}

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

TODAY = datetime.today().strftime("%Y%m%d")  # For today
day = datetime(year=1, month=1, day=1).strftime("%Y%m%d")  # For any day


# Creates a new user (Required!)
def create_user():
    user_parameters = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    response = requests.post(url=PIXELA_ENDPOINT, json=user_parameters)
    print(response.text)


# Creates a new graph
def create_graph(graph_id, name, unit, typ, color):
    graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
    graph_config = {
        "id": graph_id,
        "name": name,
        "unit": unit,
        "type": typ,  # int or float
        "color": color  # shibafu (green), momiji (red), sora (blue), ichou (yellow), ajisai (purple) and kuro (black)
    }

    response = requests.post(url=graph_endpoint, json=graph_config, headers=HEADERS)
    print(response.text)


# New entry in your graph
def new_pixel(graph_id, quantity):
    pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}"
    pixel_config = {
        "date": day,
        "quantity": quantity
    }

    response = requests.post(url=pixel_endpoint, json=pixel_config, headers=HEADERS)
    print(response.text)


# Modifies a pixel on the selected DAY
def modify_pixel(graph_id, quantity):
    pixel_put_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}/{day}"
    pixel_put_config = {
        "quantity": quantity
    }

    response = requests.put(url=pixel_put_endpoint, json=pixel_put_config, headers=HEADERS)
    print(response.text)


# Deletes a pixel on the selected DAY
def delete_pixel(graph_id):
    delete_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}/{day}"
    response = requests.delete(url=delete_pixel_endpoint, headers=HEADERS)
    print(response.text)


# Write your code here
