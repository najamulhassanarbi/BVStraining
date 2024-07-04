# weather_parser.py

import os
import re
from datetime import datetime
from weather_data import WeatherData
import pandas as pd


def parse_file(file_path):
    readings = []
    data = pd.read_csv(file_path)
    # print(data)
    if 'PKST' in data.columns:
        data.rename(columns={'PKST': 'PKT'}, inplace=True)
    data = data[["PKT", "Max TemperatureC", "Mean TemperatureC", "Min TemperatureC", "Max Humidity", " Mean Humidity",
                 " Min Humidity"]]
    # print(data.dtypes)
    data.rename(columns={"PKT": "date"}, inplace=True)
    data.dropna(inplace=True)
    for index, row in data.iterrows():
        date = datetime.strptime(row["date"], "%Y-%m-%d")
        max_temp = row["Max TemperatureC"]
        mean_temp = row["Mean TemperatureC"]
        min_temp = row["Min TemperatureC"]
        max_humidity = row["Max Humidity"]
        mean_humidity = row[" Mean Humidity"]
        min_humidity = row[" Min Humidity"]
        reading = WeatherData(date, max_temp, mean_temp, min_temp, max_humidity, mean_humidity, min_humidity)
        readings.append(reading)
    return readings


month_map = {
    1: 'Jan',
    2: 'Feb',
    3: 'Mar',
    4: 'Apr',
    5: 'May',
    6: 'Jun',
    7: 'Jul',
    8: 'Aug',
    9: 'Sep',
    10: 'Oct',
    11: 'Nov',
    12: 'Dec'
}


class WeatherParser:
    def __init__(self, files_dir):
        self.files_dir = files_dir

    def parse_files_year_wise(self, year):
        # lahore_weather_year
        all_readings = []
        for filename in os.listdir(self.files_dir):
            if filename.startswith(f'lahore_weather_{year}'):
                file_path = os.path.join(self.files_dir, filename)
                readings = parse_file(file_path)
                all_readings.extend(readings)
        return all_readings

    def parse_files_month_wise(self, year, month):
        all_readings = []

        month = month_map[month]
        for filename in os.listdir(self.files_dir):
            if filename.startswith(f'lahore_weather_{year}_{month}'):
                file_path = os.path.join(self.files_dir, filename)
                readings = parse_file(file_path)
                all_readings.extend(readings)
        return all_readings
