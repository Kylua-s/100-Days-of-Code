# Exercise 60 - Newsletter
"""
The goal is to automatically fill out the field and subscribe to the newsletter.
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

FIRST_NAME = "YOUR FIRST NAME"
LAST_NAME = "YOUR LAST NAME"
EMAIL = "YOUR EMAIL ADRESS"

# It opens a new Chrome browser window with the specified URL
driver = webdriver.Chrome()
driver.get("http://secure-retreat-92358.herokuapp.com")

# Finds the input element for the first name field and enters your first name
fName = driver.find_element(By.NAME, "fName")
fName.send_keys(FIRST_NAME)

# Finds the input element for the last name field and enters your last name
lName = driver.find_element(By.NAME, "lName")
lName.send_keys(LAST_NAME)

# Finds the input element for the email adress field and enters your email adress
email = driver.find_element(By.NAME, "email")
email.send_keys(EMAIL)

# Finds the button and clicks it
button = driver.find_element(By.CLASS_NAME, "btn")
button.click()

# Pauses the execution for 3 seconds to allow the website to process the data
time.sleep(3)

# Closes the browser
driver.quit()
