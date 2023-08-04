# Project 44 - X Bot
"""

"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

PROMISED_DOWN = 100
PROMISED_UP = 50
EMAIL = "stephanpunktmultani@gmail.com"
PASSWORD = "YOUR PASSWORD"


def get_internet_speed():
    # It opens a new Chrome browser window with the specified URL
    driver = webdriver.Chrome()
    driver.get("https://www.speedtest.net")

    time.sleep(2)

    # Declines Cookies
    driver.find_element(By.ID, "onetrust-pc-btn-handler").click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="onetrust-pc-sdk"]/div/div[3]/div[1]/button').click()
    time.sleep(2)

    # Starts the speed test
    driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
    time.sleep(45)

    dowload = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                            '3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text

    upload = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div['
                                           '3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    x(dowload, upload)
    driver.quit()


def x(download, upload):
    # It opens a new Chrome browser window with the specified URL
    driver = webdriver.Chrome()
    driver.get("https://www.x.com")

    time.sleep(2)

    # Login
    driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div['
                                  '5]/a/div/span/span').click()
    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div['
                                  '2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(EMAIL)

    driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div['
                                  '2]/div/div/div/div[6]/div/span/span').click()
    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div['
                                  '2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(PASSWORD)

    time.sleep(2)

    # Post/ Tweet or whatever it's called now
    tweet = (f"Hey Internet Provider, why is my internet speed {download}down/{upload}up when I pay for {PROMISED_DOWN}"
             f"down/{PROMISED_UP}up?")
    post = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div['
                                         '3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div['
                                         '2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
    post.send_keys(tweet)
    driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div['
                                  '2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/span/span').click()


get_internet_speed()
