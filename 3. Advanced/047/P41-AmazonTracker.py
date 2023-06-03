"""This Python code is designed to track the price of a specific product on Amazon and send an email notification
when the price falls below a specified threshold."""
import smtplib
import requests
from bs4 import BeautifulSoup

SMTP_ADDRESS = "YOUR_SMTP_ADDRESS"  # SMTP server address for sending emails
EMAIL = "YOUR_EMAIL"  # Your email address
PASSWORD = "YOUR_PASSWORD"  # Your email password
BUY_PRICE = 1  # The maximum price at which you want to be notified
URL = "https://www.amazon.com/..........."  # The URL of the Amazon product you want to track

# Sets up the header with User-Agent and Accept-Language to mimic a browser request
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(URL, headers=header)
soup = BeautifulSoup(response.content, "lxml")

# Extracts the price of the product
price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
if price_as_float < BUY_PRICE:
    # Constructing an email message with the product title and current price
    message = f"{title} is now {price}"

    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )
