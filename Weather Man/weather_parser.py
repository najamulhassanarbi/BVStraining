"""
weather_parser.py

This module defines the WeatherParser class, which parses weather data files year-wise and month-wise for Lahore,
Pakistan.

Classes:
- WeatherParser: A class to parse weather data files year-wise and month-wise from a specified directory.

"""

import os
from datetime import datetime

import pandas as pd

from constants import MONTH_MAP
from weather_data import WeatherData


class WeatherParser:
    """
        A class to parse weather data files year-wise and month-wise from a specified directory.

        Attributes:
            files_dir (str): Directory path where weather data files are located.

        Methods:
            parse_files_year_wise(year): Parses all weather data files for a specific year.
            parse_files_month_wise(year, month): Parses all weather data files for a specific month in a year.
        """

    def __init__(self, files_dir):
        """
        Initializes WeatherParser with the directory containing weather data files.

        Args:
            files_dir (str): Directory path where weather data files are located.
        """

        self.files_dir = files_dir

    def parse_file(self, file_path):
        """
        Parses a CSV file containing weather data and returns a WeatherData object.

        Args:
            file_path (str): Path to the CSV file containing weather data.

        Returns:
            Object: A WeatherData object containing parsed weather readings.
        """
        readings = []
        data = pd.read_csv(file_path)
        data.columns = data.columns.str.strip()
        date_col = None
        if "PKT" in data.columns:
            date_col = "PKT"
        elif "PKST" in data.columns:
            date_col = "PKST"

        required_cols = [date_col, "Max TemperatureC", "Mean TemperatureC", "Min TemperatureC", "Max Humidity",
                         "Mean Humidity",
                         "Min Humidity"]
        data = data[required_cols]
        data.dropna(inplace=True)
        for _, row in data.iterrows():
            try:
                date = datetime.strptime(row[f"{date_col}"], "%Y-%m-%d")
                max_temp = float(row.get("Max TemperatureC", 0))
                mean_temp = float(row.get("Mean TemperatureC", 0))
                min_temp = float(row.get("Min TemperatureC", 0))
                max_humidity = float(row.get("Max Humidity", 0))
                mean_humidity = float(row.get("Mean Humidity", 0))
                min_humidity = float(row.get("Min Humidity", 0))
                reading = WeatherData(date, max_temp, mean_temp, min_temp, max_humidity, mean_humidity, min_humidity)
                readings.append(reading)
            except ValueError:
                continue
        return readings

    def parse_files_year_wise(self, year):
        """
        Parses all weather data files for a specific year.

        Args:
            year (int): Year for which weather data files should be parsed.

        Returns:
            list: List of WeatherData objects containing parsed weather readings for the year.
        """
        all_readings = []
        for filename in os.listdir(self.files_dir):
            if filename.startswith(f'lahore_weather_{year}'):
                file_path = os.path.join(self.files_dir, filename)
                readings = self.parse_file(file_path)
                all_readings.extend(readings)
        return all_readings

    def parse_files_month_wise(self, year, month):
        """
        Parses all weather data files for a specific month in a year.

        Args:
            year (int): Year for which weather data files should be parsed.
            month (str): Month (in text format, e.g., 'Jan') for which weather data files should be parsed.

        Returns:
            list: List of WeatherData objects containing parsed weather readings for the month.
        """
        all_readings = []
        month = MONTH_MAP[month]
        for filename in os.listdir(self.files_dir):
            if filename.startswith(f'lahore_weather_{year}_{month}'):
                file_path = os.path.join(self.files_dir, filename)
                readings = self.parse_file(file_path)
                all_readings.extend(readings)
        return all_readings
