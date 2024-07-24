"""
weather_report.py

This module defines the WeatherReport class, which generates various reports based on weather calculation results.

Classes:
- WeatherReport: A class to generate weather reports including extremes, averages, and daily temperatures.

"""

from constants import COLORS


class WeatherReport:
    """
    A class to generate weather reports based on calculation results.

    Attributes:
        results: Calculation results object containing highest temperature, lowest temperature,
                most humid day, average highest temperature, average lowest temperature,
                and average mean humidity.

    Methods:
        generate_extreme_weather_yearly_report(): Generates a report for highest temperature, lowest temperature, and humidity extremes.
        generate_average_weather_yearly_report(): Generates a report for average highest temperature, average lowest temperature,
                                  and average mean humidity.
        generate_daily_temperatures_report(year, month): Generates a daily temperatures report for a specific year and month.
    """

    def __init__(self, calculation_results):
        """
        Initializes WeatherReport with calculation results.

        Args:
            calculation_results: Calculation results object containing weather data.
        """

        self.results = calculation_results

    def __colored_stars(self, day, min_temp, max_temp):
        """
        Adds colored stars to the console.
        Args:
            day (str): Day of the month.
            min_temp (float): Minimum temperature for the day.
            max_temp (float): Maximum temperature for the day.
        Returns:
            String containing the colored stars.
        """
        blue_color = COLORS["blue"]
        red_color = COLORS["red"]
        min_temp_stars = f"{blue_color}{'*' * int(min_temp)}\033[0m"
        max_temp_stars = f"{red_color}{'*' * int(max_temp)}\033[0m"
        return f"{day} {min_temp}C {min_temp_stars}{max_temp_stars} {max_temp}C"

    def generate_extreme_weather_yearly_report(self):
        """
        Generates a report for highest temperature, lowest temperature, and humidity extremes.
        Returns:
            String containing the report.
        """
        highest_temperature = self.results.get("highest_temperature")
        lowest_temperature = self.results.get("lowest_temperature")
        most_humid_day = self.results.get("most_humid_day")

        if highest_temperature and lowest_temperature and most_humid_day:
            highest_temp = highest_temperature.get("temperature")
            highest_day = highest_temperature.get("date")
            lowest_temp = lowest_temperature.get("temperature")
            lowest_day = lowest_temperature.get("date")
            humidity = most_humid_day.get("humidity")
            humid_day = most_humid_day.get("date")
            weather_report = (
                f"Highest: {round(highest_temp, 1)}C on {highest_day.strftime("%B")} {highest_day.strftime("%d")}\n"
                f"Lowest: {round(lowest_temp, 1)}C on {lowest_day.strftime("%B")} {lowest_day.strftime("%d")}\n"
                f"Humidity: {round(humidity, 1)}% on {humid_day.strftime("%B")} {humid_day.strftime("%d")}"
            )
        else:
            weather_report = "No data available for extremes for given input."
        return weather_report

    def generate_average_weather_yearly_report(self):
        """
        Generates a report for average highest temperature, average lowest temperature, and average mean humidity.
        Returns:
            String containing the report.

        """
        average_highest_temperature = self.results.get("average_highest_temperature")
        average_lowest_temperature = self.results.get("average_lowest_temperature")
        average_mean_humidity = self.results.get("average_mean_humidity")
        if average_highest_temperature and average_lowest_temperature and average_mean_humidity:

            weather_report = (f"Average highest: {round(average_highest_temperature, 1)}C\n"
                      f"Average lowest: {round(average_lowest_temperature, 1)}C\n"
                      f"Average humidity: {round(average_mean_humidity, 1)}%")
        else:
            weather_report = "No data available for averages for given input."
        return weather_report

    def generate_daily_temperatures_report(self, year, month):
        """
        Generates a daily temperatures report for a specific year and month.
        Args:
            year (int): Year for which the report is generated.
            month (int): Month (1-12) for which the report is generated.
        Returns:
            String containing the report.
        """
        weather_report = ""
        if not self.results:
            return "No data available for daily temperatures for given month."

        for date in self.results:
            day = date.strftime('%d')
            daily_temps = self.results.get(date)
            min_temp = daily_temps.get('min_temperature')
            max_temp = daily_temps.get('max_temperature')
            daily_temp_stars = self.__colored_stars(day, min_temp, max_temp)
            weather_report += f"{daily_temp_stars}\n"
        return weather_report
