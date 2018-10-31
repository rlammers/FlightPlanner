"""
A service for providing airports
"""
import pandas as pd
from Airport import Airport


class AirportService:
    """
    A module for getting the airports
    """

    airports = None

    @classmethod
    def read_airports_from_csv(cls, csv_filename):
        """
        Read airports from specified csv file
        """
        airports_df = pd.read_csv(csv_filename, header=0)
        airports = []
        for idx, airport in airports_df.iterrows():
            airports.append(
                Airport(
                    airport.icao,
                    airport.latitude,
                    airport.longitude,
                    airport.city
                )
            )
        return airports


    def get_airports(self):
        """
        Get list of available airports
        """
        if self.airports is None:
            self.airports = self.read_airports_from_csv('airports.csv')
        return self.airports
