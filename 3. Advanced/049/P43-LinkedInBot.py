# Project 43 - LinkedIn Bot
"""
NOTE: Do not enable 2-factor authentication/phone number verification and upload your CV.

Automatically logs in to your LinkedIn account.
Applies to all standard, 1-step applications.
Ignores the applications that require a note.
Ignores the complex, multistep applications.
"""

import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

EMAIL_PHONE = "YOUR EMAIL OR PHONE"
PASSWORD = "YOUR PASSWORD"


def abort_application():
    # Click Close Button
    close = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close.click()

    time.sleep(2)
    # Click Discard Button
    discard = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard.click()


# It opens a new Chrome browser window with the specified URL
driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3521778755&f_LF=f_AL&geoId=92000000&keywords=python"
           "%20developer&location=Worldwide&refresh=true")

time.sleep(5)

# Clicks the sign in button
sign_in = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in")
sign_in.click()

# Allows the page to load
time.sleep(5)

# Finds the username field and enters the email or phone number
email_phone = driver.find_element(By.ID, "username")
email_phone.send_keys(EMAIL_PHONE)

# Finds the password field and enters the password
password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

time.sleep(5)

# Get Listings
jobs = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# Apply for Jobs
for job in jobs:
    job.click()
    time.sleep(2)
    try:
        # Clicks apply button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Inserts email or phone number
        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(EMAIL_PHONE)

        # Check the submit button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            continue
        else:
            submit_button.click()

        time.sleep(2)

        # Clicks close button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        continue

time.sleep(5)
driver.quit()
