"""

This module defines utility constants  for weather data processing.

Constants:
- month_map (dict): A dictionary mapping month numbers (1-12) to their corresponding three-letter abbreviation.
- colors (dict): A dictionary mapping color names to ANSI escape sequences for colored output.
- EXPECTED_NUMBER_OF_ARGS (int): The expected number of command line arguments for the weatherman script.
"""
EXPECTED_NUMBER_OF_ARGS = 3

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


