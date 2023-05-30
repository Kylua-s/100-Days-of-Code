from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

# Origin city IATA code
ORIGIN_CITY_IATA = "LON"

# Create instances of required classes
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Get destination data from the data manager
sheet_data = data_manager.get_destination_data()

# Check if destination IATA codes are missing in the data
if sheet_data[0]["iataCode"] == "":
    # Get city names from the sheet data
    city_names = [row["city"] for row in sheet_data]

    # Retrieve destination codes using the flight search API
    data_manager.city_codes = flight_search.get_destination_codes(city_names)

    # Update the destination codes in the sheet data
    data_manager.update_destination_codes()

    # Get the updated destination data
    sheet_data = data_manager.get_destination_data()

# Create a dictionary of destinations with their details
destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data
}

# Calculate tomorrow's date and six months from today
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=6 * 30)

# Iterate over each destination code
for destination_code in destinations:
    # Check flights from the origin city to the current destination
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination_code,
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    print(flight.price)

    # If no flights found, continue to the next destination
    if flight is None:
        continue

    # Compare flight price with the destination's lowest price
    if flight.price < destinations[destination_code]["price"]:

        # Get customer emails from the data manager
        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        # Create a notification message with flight details
        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-" \
                  f"{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, " \
                  f"from {flight.out_date} to {flight.return_date}."

        # Add stopover information to the message if applicable
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        # Send emails to the customers with the notification message
        notification_manager.send_emails(emails, message)
