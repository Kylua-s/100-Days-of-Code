# Exercise 59 - Wikipedia
"""
The goal is to get the red underlined number.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

# It opens a new Chrome browser window with the specified URL
driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Gets and prints the number
articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
print(articles.text)

# Closes the browser
driver.quit()
