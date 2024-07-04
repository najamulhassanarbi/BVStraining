# weather_reading.py

class WeatherData:
    def __init__(self, date, max_temp, mean_temp, min_temp, dew_point, mean_dew_point,
                 min_dew_point, max_humidity, mean_humidity, min_humidity,
                 max_pressure, mean_pressure, min_pressure,
                 max_visibility, mean_visibility, min_visibility,
                 max_wind_speed, mean_wind_speed, max_gust_speed,
                 precipitation, cloud_cover, events, wind_direction):
        self.date = date
        self.max_temperature = max_temp
        self.mean_temperature = mean_temp
        self.min_temperature = min_temp
        self.dew_point = dew_point
        self.mean_dew_point = mean_dew_point
        self.min_dew_point = min_dew_point
        self.max_humidity = max_humidity
        self.mean_humidity = mean_humidity
        self.min_humidity = min_humidity
        self.max_pressure = max_pressure
        self.mean_pressure = mean_pressure
        self.min_pressure = min_pressure
        self.max_visibility = max_visibility
        self.mean_visibility = mean_visibility
        self.min_visibility = min_visibility
        self.max_wind_speed = max_wind_speed
        self.mean_wind_speed = mean_wind_speed
        self.max_gust_speed = max_gust_speed
        self.precipitation = precipitation
        self.cloud_cover = cloud_cover
        self.events = events
        self.wind_direction = wind_direction
