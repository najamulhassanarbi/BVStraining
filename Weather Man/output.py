"""
output.py

This module processes input arguments related to weather data analysis, validates commands,
parses weather data files, generates reports, and outputs the reports to standard output.

Classes:
- OutputResults: Handles input arguments, validates commands, parses weather data,
  calculates metrics, generates reports, and prints them.

"""

from constants import COMMANDS, MESSAGES
from input_parsing import InputParsing
from weather_parser import WeatherParser
from weather_reports import WeatherReport
from weather_calculator import WeatherCalculator


class OutputResults:
    """
    OutputResults class processes input arguments, validates commands, parses weather data, calculates weather metrics,
    generates reports based on specified commands, and prints them to standard output.

    Attributes:
        input_args (list): List of input arguments passed to the program.

    Methods:
        output():
            Validates input arguments and commands, performs respective actions based on commands,
            generates weather reports, and prints them to standard output.
    """

    def __init__(self, input_args):
        """
        Initializes an OutputResults instance.

        Args:
            input_args (list): List of input arguments passed to the program.
        """
        self.input_args = input_args

    def output(self):
        """
        Validates input arguments, processes commands, parses weather data, calculates weather metrics,
        generates reports based on specified commands, and prints them to standard output.
        """
        input_parser = InputParsing(self.input_args)
        validation_result = input_parser.validate_args()

        if not validation_result.get("is_valid"):
            return validation_result.get("message")
        files_dir = validation_result["input_arguments"].get("files_dir")
        commands = self.input_args[2:]
        input_args = validation_result["input_arguments"]

        option = 0
        while option < len(commands):
            input_args["command"] = commands[option]
            input_args["date"] = commands[option + 1]
            validation_result = input_parser.validate_commands(input_args)
            if not validation_result.get("is_valid"):
                return validation_result.get("message")
            command = input_args.get("command")
            date = input_args.get("date")

            parser = WeatherParser(files_dir)

            if command == COMMANDS.get("get_yearly_extreme_weather_values"):
                year = int(date)
                weather_data = parser.parse_files_year_wise(year)
                weather_calculator = WeatherCalculator(weather_data)
                results = weather_calculator.calculate_yearly_extremes(year)
                report = WeatherReport(results)
                output = report.generate_extreme_weather_yearly_report()
                print(output)
                option += 2
            elif command == COMMANDS.get("get_yearly_average_weather_values"):
                year, month = map(int, date.split('/'))
                weather_data = parser.parse_files_month_wise(year=year, month=month)
                weather_calculator = WeatherCalculator(weather_data)
                results = weather_calculator.calculate_monthly_averages(year, month)
                report = WeatherReport(results)
                output = report.generate_average_weather_yearly_report()
                print(output)
                option += 2
            elif command == COMMANDS.get("get_monthly_temperature_values"):
                year, month = map(int, date.split('/'))
                weather_data = parser.parse_files_month_wise(year=year, month=month)
                weather_calculator = WeatherCalculator(weather_data)
                results = weather_calculator.calculate_daily_temperatures(year, month)
                report = WeatherReport(results)
                output = report.generate_daily_temperatures_report(year, month)
                print(output)
                option += 2
            else:
                message = MESSAGES.get("invalid_command")
                return message
