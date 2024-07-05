"""

This module defines utility constants  for weather data processing.

Constants:
- month_map (dict): A dictionary mapping month numbers (1-12) to their corresponding three-letter abbreviation.
- weather_calculation_results (dict): A dictionary to store weather calculation results including highest temperature,
                                        lowest temperature, most humid day, average highest temperature, average lowest
                                        temperature, average mean humidity, and daily temperatures.
"""

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

colors = {
    "red": "\033[31m",
    "blue": "\033[34m",

}

weather_calculation_results = {
    'highest_temperature': None,
    'lowest_temperature': None,
    'most_humid_day': None,
    'average_highest_temperature': None,
    'average_lowest_temperature': None,
    'average_mean_humidity': None,
    'daily_temperatures': []
}
