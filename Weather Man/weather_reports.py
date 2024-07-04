# weather_report.py
from datetime import datetime


class WeatherReport:
    def __init__(self, calculation_results):
        self.results = calculation_results

    def generate_extremes_report(self):
        if self.results.highest_temperature:
            highest_temp, highest_day = self.results.highest_temperature
            print(f"Highest: {highest_temp}C on {highest_day.strftime('%B %d')}")
        if self.results.lowest_temperature:
            lowest_temp, lowest_day = self.results.lowest_temperature
            print(f"Lowest: {lowest_temp}C on {lowest_day.strftime('%B %d')}")
        if self.results.most_humid_day:
            humidity, humid_day = self.results.most_humid_day
            print(f"Humidity: {humidity}% on {humid_day.strftime('%B %d')}")

    def generate_averages_report(self):
        if self.results.average_highest_temperature is not None:
            print(f"Highest Average: {self.results.average_highest_temperature:.1f}C")
        if self.results.average_lowest_temperature is not None:
            print(f"Lowest Average: {self.results.average_lowest_temperature:.1f}C")
        if self.results.average_mean_humidity is not None:
            print(f"Average Mean Humidity: {self.results.average_mean_humidity:.1f}%")

    def generate_daily_temperatures_report(self, year, month):
        month_name = datetime(year, month, 1).strftime('%B')
        print(f"{month_name} {year}")
        for date, max_temp, min_temp in self.results.daily_temperatures:
            day = date.strftime('%d')
            print(f"{day} {'+' * int(max_temp)} {int(max_temp)}C")
            print(f"{day} {'+' * int(min_temp)} {int(min_temp)}C")
