"""
A service for providing airports
"""
import pandas as pd
from airport import Airport


class AirportService:
    """
    A module for getting the airports
    """

    airports = None

    def __init__(self):
        self.airports = self.read_airports_from_csv('airports.csv')

    @classmethod
    def read_airports_from_csv(cls, csv_filename):
        """
        Read airports from specified csv file
        """
        airports_df = pd.read_csv(csv_filename)
        airports = []
        
        for row in airports_df.itertuples(index=False, name="Aiport"):
            airports.append(
                Airport(
                    row.icao,
                    row.latitude,
                    row.longitude,
                    row.city
                )
            )
  
        return airports


    def get_airports(self):
        """
        Get list of available airports
        """
        return self.airports

    def get_airport(self, icao):
        for airport in self.airports:
            if airport.icao == icao:
                return airport

