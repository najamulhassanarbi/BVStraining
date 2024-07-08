"""
weather_report.py

This module defines the WeatherReport class, which generates various reports based on weather calculation results.

Classes:
- WeatherReport: A class to generate weather reports including extremes, averages, and daily temperatures.

"""

from datetime import datetime
from constants import colors


class WeatherReport:
    """
    A class to generate weather reports based on calculation results.

    Attributes:
    - results: Calculation results object containing highest temperature, lowest temperature,
                most humid day, average highest temperature, average lowest temperature,
                and average mean humidity.

    Methods:
    - generate_extreme_weather_yearly_report(): Generates a report for highest temperature, lowest temperature, and humidity extremes.
    - generate_average_weather_yearly_report(): Generates a report for average highest temperature, average lowest temperature,
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

    def __colored_stars(self, day, min_temp, max_temp):
        """
        Adds colored stars to the console.
        Args:
        - num_stars: Number of stars to print.
        - color: Color of the stars.
        Returns:
        - String containing the colored stars.
        """
        blue_color = colors["blue"]
        red_color = colors["red"]
        min_temp_stars = f"{blue_color}{'*' * int(min_temp)}\033[0m"
        max_temp_stars = f"{red_color}{'*' * int(max_temp)}\033[0m"
        print(min_temp_stars)
        return f"{day} {min_temp}C {min_temp_stars}{max_temp_stars} {max_temp}C"

    def generate_extreme_weather_yearly_report(self):
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
            output = (
                f"Highest: {round(highest_temp, 1)}C on {highest_day.strftime("%B")} {highest_day.strftime("%d")}\n"
                f"Lowest: {round(lowest_temp, 1)}C on {lowest_day.strftime("%B")} {lowest_day.strftime("%d")}\n"
                f"Humidity: {round(humidity, 1)}% on {humid_day.strftime("%B")} {humid_day.strftime("%d")}"
            )
        else:
            output = "No data available for extremes for given input."
        return output

    def generate_average_weather_yearly_report(self):
        """
        Generates a report for average highest temperature, average lowest temperature, and average mean humidity.

        """
        output = ""
        if (self.results["average_highest_temperature"]
                and self.results["average_lowest_temperature"]
                and self.results["average_mean_humidity"]):

            output = (f"Average highest: {round(self.results['average_highest_temperature'], 1)}C\n"
                      f"Average lowest: {round(self.results['average_lowest_temperature'], 1)}C\n"
                      f"Average humidity: {round(self.results['average_mean_humidity'], 1)}%")
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
        output = ""
        for date, max_temp, min_temp in self.results["daily_temperatures"]:
            day = date.strftime('%d')
            daily_temp_stars = self.__colored_stars(day, min_temp, max_temp)
            output += f"{daily_temp_stars}\n"
        return output
