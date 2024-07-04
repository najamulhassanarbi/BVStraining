# weather_calculator.py

from datetime import datetime
from weathercalculationsresults import WeatherCalculationResults


class WeatherCalculator:
    def __init__(self, weather_data):
        self.weather_data = weather_data

    def calculate_yearly_extremes(self, year):
        year_data = self.weather_data
        results = WeatherCalculationResults()

        if not year_data:
            print("No data found for the year")
            return results

        highest_temp = max(year_data, key=lambda x: x.max_temperature)
        lowest_temp = min(year_data, key=lambda x: x.min_temperature)
        most_humid_day = max(year_data, key=lambda x: x.max_humidity)

        results.highest_temperature = (highest_temp.max_temperature, highest_temp.date)
        results.lowest_temperature = (lowest_temp.min_temperature, lowest_temp.date)
        results.most_humid_day = (most_humid_day.max_humidity, most_humid_day.date)

        return results

    def calculate_monthly_averages(self, year, month):
        month_data = self.weather_data
        results = WeatherCalculationResults()

        if not month_data:
            print(f'No data found for the {year}-{month}')
            return results

        results.average_highest_temperature = sum(d.max_temperature for d in month_data) / len(month_data)
        results.average_lowest_temperature = sum(d.min_temperature for d in month_data) / len(month_data)
        results.average_mean_humidity = sum(d.mean_humidity for d in month_data) / len(month_data)

        return results

    def calculate_daily_temperatures(self, year, month):
        month_data = self.weather_data
        results = WeatherCalculationResults()

        if not month_data:
            print(f'No data found for the {year}-{month}')
            return results

        results.daily_temperatures = [(d.date, d.max_temperature, d.min_temperature) for d in month_data]

        return results
