import requests

# Define the endpoints for Sheety
SHEETY_PRICES_ENDPOINT = "YOUR SHEETY PRICES ENDPOINT"
SHEETY_USERS_ENDPOINT = "YOUR SHEETY USERS ENDPOINT"


# Create a DataManager class to handle data operations
class DataManager:

    def __init__(self):
        # Initialize empty dictionaries to store customer and destination data
        self.customer_data = {}
        self.destination_data = {}

    # Fetch destination data from the Sheety prices endpoint
    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        # Extract and store the destination data from the response
        self.destination_data = data["prices"]
        return self.destination_data

    # Update destination codes using the destination data
    def update_destination_codes(self):
        # Iterate over each city in the destination data
        for city in self.destination_data:
            # Create a new data dictionary with the updated IATA code
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            # Send a PUT request to update the destination code for the city
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            # Print the response text to check if the update was successful
            print(response.text)

    # Fetch customer emails from the Sheety users endpoint
    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(url=customers_endpoint)
        data = response.json()
        # Extract and store the customer data from the response
        self.customer_data = data["users"]
        return self.customer_data
