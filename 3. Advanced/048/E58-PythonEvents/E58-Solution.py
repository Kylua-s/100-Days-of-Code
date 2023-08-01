# Exercise 58 - Python Eventes
"""
The goal is to get and format the upcoming events into a dictionary.
The structure should be {0: {'time': "the actual date", 'name': "the name of the event"}, 1: {...}}.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

# It opens a new Chrome browser window with the specified URL
driver = webdriver.Chrome()
driver.get("https://www.python.org")

# Gets all the upcoming events and formats the events into a list
elements = driver.find_elements(By.CSS_SELECTOR, '.event-widget ul')
events = [element.text for element in elements][0].split('\n')

# Formats the list into the desired format
num = 0
formatted_events = {}
for i in range(0, len(events), 2):
    formatted_events[num] = {'time': events[i], 'name': events[i + 1]}
    num += 1

print(formatted_events)

# Closes the browser
driver.quit()
