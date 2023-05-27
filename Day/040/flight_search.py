import requests
from flight_data import FlightData
from pprint import pprint

# Tequila API endpoint and API key
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "YOUR FLIGHT SEARCH API KEY"


class FlightSearch:

    # Get the destination code for a given city name using Tequila API
    def get_destination_codes(self, city_name):
        # Tequila locations endpoint for querying destination codes
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"

        # Set request headers with the API key
        headers = {"apikey": TEQUILA_API_KEY}

        # Set query parameters with the city name and location type
        query = {"term": city_name, "location_types": "city"}

        # Send a GET request to the location endpoint with headers and query parameters
        response = requests.get(url=location_endpoint, headers=headers, params=query)

        # Parse the response JSON and extract the location results
        results = response.json()["locations"]

        # Get the destination code from the first location result
        code = results[0]["code"]

        return code

    # Check flights between the given origin and destination using Tequila API
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        # Set request headers with the API key
        headers = {"apikey": TEQUILA_API_KEY}

        # Set query parameters with flight search details
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        # Send a GET request to the flight search endpoint with headers and query parameters
        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )

        try:
            # Try to extract flight data from the response JSON
            data = response.json()["data"][0]
        except IndexError:
            # If no direct flights are found, update query parameters to allow one stopover
            query["max_stopovers"] = 1
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/v2/search",
                headers=headers,
                params=query,
            )
            data = response.json()["data"][0]

            # Print the flight data for debugging
            pprint(data)

            # Create a FlightData object with the flight details including stopover information
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )

            return flight_data
        else:
            # Create a FlightData object with the flight details for direct flights
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )

            return flight_data
