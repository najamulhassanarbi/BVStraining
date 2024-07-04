"""
weather_report.py

This module defines the WeatherReport class, which generates various reports based on weather calculation results.

Classes:
- WeatherReport: A class to generate weather reports including extremes, averages, and daily temperatures.

"""

from datetime import datetime
from utils import print_colored_stars


class WeatherReport:
    """
    A class to generate weather reports based on calculation results.

    Attributes:
    - results: Calculation results object containing highest temperature, lowest temperature,
                most humid day, average highest temperature, average lowest temperature,
                and average mean humidity.

    Methods:
    - generate_extremes_report(): Generates a report for highest temperature, lowest temperature, and humidity extremes.
    - generate_averages_report(): Generates a report for average highest temperature, average lowest temperature,
                                  and average mean humidity.
    - generate_daily_temperatures_report(year, month): Generates a daily temperatures report for a specific year and month.
    """

    def __init__(self, calculation_results):
        """
        Initializes WeatherReport with calculation results.

        Args:
        - calculation_results: Calculation results object containing weather data.
        """

        self.results = calculation_results

    def generate_extremes_report(self):
        """
        Generates a report for highest temperature, lowest temperature, and humidity extremes.
        Returns:
        - String containing the report.
        """
        output = ""

        if (self.results["highest_temperature"]
                and self.results["lowest_temperature"]
                and self.results["most_humid_day"]):
            highest_temp, highest_day = self.results["highest_temperature"]
            lowest_temp, lowest_day = self.results["lowest_temperature"]
            humidity, humid_day = self.results["most_humid_day"]
            output = (f"Highest: {highest_temp}C on {highest_day}\n"
                      f"Lowest: {lowest_temp}C on {lowest_day}\n"
                      f"Humidity: {humidity}% on {humid_day}"
                      )
        else:
            output = "No data available for extremes for given input."
        return output

    def generate_averages_report(self):
        """
        Generates a report for average highest temperature, average lowest temperature, and average mean humidity.

        """
        output = ""
        if (self.results["average_highest_temperature"]
                and self.results["average_lowest_temperature"]
                and self.results["average_mean_humidity"]):

            output = (f"Average highest: {self.results['average_highest_temperature']}C\n"
                      f"Average lowest: {self.results['average_lowest_temperature']}C\n"
                      f"Average humidity: {self.results['average_mean_humidity']}%")
        else:
            output = "No data available for averages for given input."
        return output

    def generate_daily_temperatures_report(self, year, month):
        """
        Generates a daily temperatures report for a specific year and month.

        Args:
        - year (int): Year for which the report is generated.
        - month (int): Month (1-12) for which the report is generated.
        """

        month_name = datetime(year, month, 1).strftime('%B')
        output = ""
        for date, max_temp, min_temp in self.results["daily_temperatures"]:
            day = date.strftime('%d')
            blue_stars = print_colored_stars(min_temp, "blue")
            red_stars = print_colored_stars(max_temp, "red")
            output += f"{day} {min_temp}{blue_stars}{red_stars}{max_temp}\n"
        return output
