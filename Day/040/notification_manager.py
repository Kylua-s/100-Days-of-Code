import smtplib
from twilio.rest import Client

# Twilio configuration
TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"
TWILIO_VIRTUAL_NUMBER = "YOUR TWILIO VIRTUAL NUMBER"
TWILIO_VERIFIED_NUMBER = "YOUR TWILIO VERIFIED NUMBER"

# Email configuration
MAIL_PROVIDER_SMTP_ADDRESS = "YOUR EMAIL PROVIDER SMTP ADDRESS smtp.gmail.com"
MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"


class NotificationManager:

    def __init__(self):
        # Initialize Twilio client with account SID and auth token
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    # Send an SMS using Twilio
    def send_sms(self, message):
        # Create a new message using the Twilio client
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Print the message SID for reference
        print(message.sid)

    # Send emails to a list of recipients
    def send_emails(self, emails, message):
        # Establish an SMTP connection with the email provider
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            # Start a secure TLS connection
            connection.starttls()
            # Login to the email account
            connection.login(MY_EMAIL, MY_PASSWORD)
            # Iterate over each email address in the recipients list
            for email in emails:
                # Send the email with the specified subject and message
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
