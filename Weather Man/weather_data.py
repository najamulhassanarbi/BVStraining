# weather_reading.py

class WeatherData:
    def __init__(self, date, max_temp, mean_temp, min_temp, max_humidity, mean_humidity, min_humidity):
        self.date = date
        self.max_temperature = max_temp
        self.mean_temperature = mean_temp
        self.min_temperature = min_temp
        self.max_humidity = max_humidity
        self.mean_humidity = mean_humidity
        self.min_humidity = min_humidity

    def __str__(self):
        return f'{self.date}, {self.max_temperature}, {self.mean_temperature}, {self.min_temperature}, {self.max_humidity}, {self.mean_humidity}, {self.min_humidity}'
