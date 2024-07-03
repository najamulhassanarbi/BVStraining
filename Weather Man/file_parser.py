# weather_parser.py

import os
import re
from datetime import datetime
from weather_data import WeatherData

class WeatherParser:
    def __init__(self, files_dir):
        self.files_dir = files_dir
    
    def parse_files(self):
        all_readings = []
        for filename in os.listdir(self.files_dir):
            if filename.startswith('lahore_weather'):
                file_path = os.path.join(self.files_dir, filename)
                readings = self.parse_file(file_path)
                all_readings.extend(readings)
        return all_readings

    
    def parse_file(self, file_path):
        readings = []
        with open(file_path, 'r') as file:
            next(file)
            next(file) 
            for line in file:
                data = line.strip().split(',')
                # print(len(data))
                if len(data) == 23:  
                    # print(data)
                    date_str = data[0]
                    max_temp = float(data[1].strip() or 0) 
                    mean_temp = float(data[2].strip() or 0)
                    min_temp = float(data[3].strip() or 0)
                    dew_point = float(data[4].strip() or 0)
                    mean_dew_point = float(data[5].strip() or 0)
                    min_dew_point = float(data[6].strip() or 0)
                    max_humidity = float(data[7].strip() or 0)
                    mean_humidity = float(data[8].strip() or 0)
                    min_humidity = float(data[9].strip() or 0)
                    max_pressure = float(data[10].strip() or 0)
                    mean_pressure = float(data[11].strip() or 0)
                    min_pressure = float(data[12].strip() or 0)
                    max_visibility = float(data[13].strip() or 0)
                    mean_visibility = float(data[14].strip() or 0)
                    min_visibility = float(data[15].strip() or 0)
                    max_wind_speed = float(data[16].strip() or 0)
                    mean_wind_speed = float(data[17].strip() or 0)
                    max_gust_speed = float(data[18].strip() or 0) 
                    precipitation = float(data[19].strip() or 0)
                    cloud_cover = float(data[20].strip() or 0)
                    events = data[21].strip() or ""
                    wind_direction = float(data[22].strip() or 0)
                    
                    # Create datetime object from date_str
                    date = datetime.strptime(date_str, '%Y-%m-%d')
                    
                    # Create WeatherReading object and add to list
                    reading = WeatherData(date=date, max_temp=max_temp, mean_temp=mean_temp,
                                             min_temp=min_temp, dew_point=dew_point,
                                             mean_dew_point=mean_dew_point, min_dew_point=min_dew_point,
                                             max_humidity=max_humidity, mean_humidity=mean_humidity,
                                             min_humidity=min_humidity, max_pressure=max_pressure,
                                             mean_pressure=mean_pressure, min_pressure=min_pressure,
                                             max_visibility=max_visibility, mean_visibility=mean_visibility,
                                             min_visibility=min_visibility, max_wind_speed=max_wind_speed,
                                             mean_wind_speed=mean_wind_speed, max_gust_speed=max_gust_speed,
                                             precipitation=precipitation, cloud_cover=cloud_cover,
                                             events=events, wind_direction=wind_direction)
                    readings.append(reading)
        return readings
