"""

This module defines utility constants  for weather data processing.

Constants:
- MONTH_MAP (dict): A dictionary mapping month numbers (1-12) to their corresponding three-letter abbreviation.
- COLORS (dict): A dictionary mapping color names to ANSI escape sequences for colored output.
- EXPECTED_NUMBER_OF_ARGS (int): The expected number of command line arguments for the weatherman script.
- COMMANDS (dict): A dictionary mapping strings to commands.
- MESSAGES (dict): A dictionary mapping error to messages
"""

EXPECTED_NUMBER_OF_ARGS = 4

COMMANDS = {
    "get_yearly_extreme_weather_values": '-e',
    "get_yearly_average_weather_values": '-a',
    "get_monthly_temperature_values": '-c',
}

MESSAGES = {
    'error_for_year': "Error: Year must be between 1996 and 2011",
    'error_for_date': "Error: Year must be between 1996 and 2011 Year and Month must be between 01 and 12. Plz "
                      "provide them in YYYY/MM format after command",
    "usage": "Usage: weatherman.py /path/to/files-dir -e 2002 or -a 2002/3 or -c 2002/12",
    "file_error": "Error:  is not a valid directory",
    "invalid": "Invalid option",
    "valid": "validated"
}

MONTH_MAP = {
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

COLORS = {
    "red": "\033[31m",
    "blue": "\033[34m",

}
