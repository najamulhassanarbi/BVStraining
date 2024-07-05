"""
weather_parser.py

This module defines the WeatherParser class, which parses weather data files year-wise and month-wise for Lahore,
Pakistan.

Classes:
- WeatherParser: A class to parse weather data files year-wise and month-wise from a specified directory.

"""

import os
from constants import month_map
from utils import parse_file


class WeatherParser:
    """
        A class to parse weather data files year-wise and month-wise from a specified directory.

        Attributes:
        - files_dir (str): Directory path where weather data files are located.

        Methods:
        - parse_files_year_wise(year): Parses all weather data files for a specific year.
        - parse_files_month_wise(year, month): Parses all weather data files for a specific month in a year.
        """

    def __init__(self, files_dir):
        """
        Initializes WeatherParser with the directory containing weather data files.

        Args:
        - files_dir (str): Directory path where weather data files are located.
        """

        self.files_dir = files_dir

    def parse_files_year_wise(self, year):
        """
        Parses all weather data files for a specific year.

        Args:
        - year (int): Year for which weather data files should be parsed.

        Returns:
        - list: List of WeatherData objects containing parsed weather readings for the year.
        """
        # lahore_weather_year
        all_readings = []
        for filename in os.listdir(self.files_dir):
            if filename.startswith(f'lahore_weather_{year}'):
                file_path = os.path.join(self.files_dir, filename)
                readings = parse_file(file_path)
                all_readings.extend(readings)
        return all_readings

    def parse_files_month_wise(self, year, month):
        """
        Parses all weather data files for a specific month in a year.

        Args:
        - year (int): Year for which weather data files should be parsed.
        - month (str): Month (in text format, e.g., 'Jan') for which weather data files should be parsed.

        Returns:
        - list: List of WeatherData objects containing parsed weather readings for the month.
        """
        all_readings = []
        month = month_map[month]
        for filename in os.listdir(self.files_dir):
            if filename.startswith(f'lahore_weather_{year}_{month}'):
                file_path = os.path.join(self.files_dir, filename)
                readings = parse_file(file_path)
                all_readings.extend(readings)
        return all_readings
