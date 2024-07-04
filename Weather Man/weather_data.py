"""
weather_reading.py

This module defines the WeatherData class, which represents a single weather reading with attributes for date,
temperature, and humidity.

Classes:
- WeatherData: A class to represent weather data for a specific date, including temperatures and humidity levels.

"""


class WeatherData:
    """
    A class to represent weather data for a specific date.

    Attributes:
    - date (datetime): The date of the weather data.
    - max_temperature (float): The maximum temperature recorded on this date.
    - mean_temperature (float): The mean temperature recorded on this date.
    - min_temperature (float): The minimum temperature recorded on this date.
    - max_humidity (float): The maximum humidity recorded on this date.
    - mean_humidity (float): The mean humidity recorded on this date.
    - min_humidity (float): The minimum humidity recorded on this date.

    Methods:
    - __str__(): Returns a string representation of the weather data.
    """

    def __init__(self, date, max_temp, mean_temp, min_temp, max_humidity, mean_humidity, min_humidity):
        """
        Initializes a WeatherData instance with the provided attributes.

        Args:
        - date (datetime): The date of the weather data.
        - max_temp (float): The maximum temperature recorded on this date.
        - mean_temp (float): The mean temperature recorded on this date.
        - min_temp (float): The minimum temperature recorded on this date.
        - max_humidity (float): The maximum humidity recorded on this date.
        - mean_humidity (float): The mean humidity recorded on this date.
        - min_humidity (float): The minimum humidity recorded on this date.
        """
        self.date = date
        self.max_temperature = max_temp
        self.mean_temperature = mean_temp
        self.min_temperature = min_temp
        self.max_humidity = max_humidity
        self.mean_humidity = mean_humidity
        self.min_humidity = min_humidity

    def __str__(self):
        """
        Returns a string representation of the weather data.

        Returns:
        - str: A string representing the weather data.
        """

        return f'{self.date}, {self.max_temperature}, {self.mean_temperature}, {self.min_temperature}, {self.max_humidity}, {self.mean_humidity}, {self.min_humidity}'
