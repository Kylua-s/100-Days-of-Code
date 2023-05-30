class FlightData:

    def __init__(
            self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date,
            stop_overs=0, via_city=""):
        # Initialize the FlightData object with the given parameters

        # Price of the flight
        self.price = price

        # Origin city of the flight
        self.origin_city = origin_city

        # Origin airport code of the flight
        self.origin_airport = origin_airport

        # Destination city of the flight
        self.destination_city = destination_city

        # Destination airport code of the flight
        self.destination_airport = destination_airport

        # Outbound date of the flight
        self.out_date = out_date

        # Return date of the flight
        self.return_date = return_date

        # Number of stopovers in the flight (default is 0)
        self.stop_overs = stop_overs

        # City where the flight has stopovers (if any)
        self.via_city = via_city
