"""
weather_calculator.py

This module defines the WeatherCalculator class, which performs calculations on weather data to generate yearly extremes,
monthly averages, and daily temperatures.

Classes:
- WeatherCalculator: A class to calculate weather extremes, averages, and daily temperatures based on provided weather data.

"""

from collections import defaultdict


class WeatherCalculator:
    """
    A class to perform calculations on weather data and generate reports.

    Attributes:
        weather_data: Weather data containing temperature and humidity information.

    Methods:
        calculate_yearly_extremes(year): Calculates yearly extremes (highest temperature, lowest temperature,
                                        most humid day) for the specified year.
        calculate_monthly_averages(year, month): Calculates monthly averages (highest temperature, lowest temperature,
                                                mean humidity) for the specified year and month.
        calculate_daily_temperatures(year, month): Retrieves daily temperatures for the specified year and month.
    """

    def __init__(self, weather_data):
        """
        Initializes WeatherCalculator with weather data.

        Args:
            weather_data (list): List of weather data objects containing temperature and humidity information.
        """
        self.weather_data = weather_data

    def calculate_yearly_extremes(self, year):
        """
        Calculates yearly extremes (highest temperature, lowest temperature, most humid day) for the specified year.

        Args:
            year (int): Year for which extremes are calculated.

        Returns:
            WeatherCalculationResults: Object containing calculated extremes.
        """

        year_data = self.weather_data
        yearly_weather_extremes_calculation_results = defaultdict(lambda: defaultdict(int))
        if not year_data:
            return yearly_weather_extremes_calculation_results
        highest_temp = None
        lowest_temp = None
        most_humid_day = None
        for day in year_data:
            if highest_temp is None or day.max_temperature > highest_temp.max_temperature:
                highest_temp = day
            if lowest_temp is None or day.min_temperature < lowest_temp.min_temperature:
                lowest_temp = day
            if most_humid_day is None or day.max_humidity > most_humid_day.max_humidity:
                most_humid_day = day
                
        yearly_weather_extremes_calculation_results["highest_temperature"]["temperature"] = highest_temp.max_temperature
        yearly_weather_extremes_calculation_results["highest_temperature"]["date"] = highest_temp.date
        yearly_weather_extremes_calculation_results["lowest_temperature"]["temperature"] = lowest_temp.min_temperature
        yearly_weather_extremes_calculation_results["lowest_temperature"]["date"] = lowest_temp.date
        yearly_weather_extremes_calculation_results["most_humid_day"]["humidity"] = most_humid_day.max_humidity
        yearly_weather_extremes_calculation_results["most_humid_day"]["date"] = most_humid_day.date
        return yearly_weather_extremes_calculation_results

    def calculate_monthly_averages(self, year, month):
        """
        Calculates monthly averages (highest temperature, lowest temperature, mean humidity) for the specified year
        and month.

        Args:
            year (int): Year for which averages are calculated.
            month (int): Month (1-12) for which averages are calculated.

        Returns:
            WeatherCalculationResults: Object containing calculated averages.
        """

        month_data = self.weather_data
        monthly_average_weather_calculation_results = defaultdict(float)

        if not month_data:
            return monthly_average_weather_calculation_results

        monthly_average_weather_calculation_results["average_highest_temperature"] = (
                sum(day_data.max_temperature for day_data in month_data) / len(month_data)
        )
        monthly_average_weather_calculation_results["average_lowest_temperature"] = (
                sum(day_data.min_temperature for day_data in month_data) / len(month_data)
        )
        monthly_average_weather_calculation_results["average_mean_humidity"] = (
                sum(day_data.mean_humidity for day_data in month_data) / len(month_data)
        )

        return monthly_average_weather_calculation_results

    def calculate_daily_temperatures(self, year, month):
        """
        Retrieves daily temperatures for the specified year and month.

        Args:
            year (int): Year for which daily temperatures are retrieved.
            month (int): Month (1-12) for which daily temperatures are retrieved.

        Returns:
            WeatherCalculationResults: dictionary containing daily temperatures.
        """
        month_data = self.weather_data
        weather_calculation_results = defaultdict(lambda: defaultdict(float))

        if not month_data:
            return weather_calculation_results

        for day_data in month_data:
            weather_calculation_results[day_data.date]["max_temperature"] = day_data.max_temperature
            weather_calculation_results[day_data.date]["min_temperature"] = day_data.min_temperature

        return weather_calculation_results
