# Project 42 - Cookie Clicker
"""
The goal is to create a bot that plays Cookie Clicker.
Every 5 seconds, the bot will check the right pane to see which upgrades are affordable and buy the most expensive one.
After 5 minutes, the bot will stop and print the cookies per second value.
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# It opens a new Chrome browser window with the specified URL
driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/experiments/cookie/")


# Function to determine the next upgrade check time
def upgrade_check():
    return time.time() + 5


# Function to determine when the script should stop (after 5 minutes)
def stop():
    return time.time() + 60 * 5


# Function to buy the best affordable upgrade
def buy_upgrades():
    # Gets the player money
    money = int(driver.find_element(By.ID, "money").text.replace(',', ''))

    # Stores upgrade information in a dictionary
    upgrades = {
        "buyCursor": int(driver.find_element(By.ID, "buyCursor").text.replace(',', '').split()[2]),
        "buyGrandma": int(driver.find_element(By.ID, "buyGrandma").text.replace(',', '').split()[2]),
        "buyFactory": int(driver.find_element(By.ID, "buyFactory").text.replace(',', '').split()[2]),
        "buyMine": int(driver.find_element(By.ID, "buyMine").text.replace(',', '').split()[2]),
        "buyShipment": int(driver.find_element(By.ID, "buyShipment").text.replace(',', '').split()[2]),
        "buyAlchemy lab": int(driver.find_element(By.ID, "buyAlchemy lab").text.replace(',', '').split()[3]),
        "buyPortal": int(driver.find_element(By.ID, "buyPortal").text.replace(',', '').split()[2]),
        "buyTime machine": int(driver.find_element(By.ID, "buyTime machine").text.replace(',', '').split()[3])
    }

    # Find the highest affordable upgrade
    max_value = 0
    for value in upgrades.values():
        if max_value < value <= money:
            max_value = value

    # Buys the highest affordable upgrade
    for key, value in upgrades.items():
        if value == max_value:
            upgrade = driver.find_element(By.ID, key)
            upgrade.click()


# Get the initial upgrade check time and the time to stop
now = upgrade_check()
stop = stop()
while True:
    # Click the cookie to collect cookies
    cookie = driver.find_element(By.ID, "cookie")
    cookie.click()

    # Check if it's time to do an upgrade check
    if time.time() > now:
        buy_upgrades()
        now = upgrade_check()

    # Check if it's time to stop the script
    if time.time() > stop:
        break

# Print the cookies per second value
print(driver.find_element(By.ID, "cps").text)
