"""
weatherman.py

This module is the main entry point for the WeatherMan application

Usage:
- python weatherman.py <files_dir> <options>

"""
import sys

from input_parsing import InputParsing
from weather_parser import WeatherParser
from weather_reports import WeatherReport
from weather_calculator import WeatherCalculator


def main():
    input_parser = InputParsing(sys.argv)
    is_valid, message, input_args = input_parser.validate_args()

    if not is_valid:
        print(message)
        sys.exit(1)

    files_dir = input_args.get("files_dir")
    command = input_args.get("command")
    date = input_args.get("date")

    parser = WeatherParser(files_dir)

    if command == '-e':
        year = int(date)
        weather_data = parser.parse_files_year_wise(year)
        weather_calculator = WeatherCalculator(weather_data)
        results = weather_calculator.calculate_yearly_extremes(year)
        report = WeatherReport(results)
        output = report.generate_extreme_weather_yearly_report()
        print(output)
    elif command == '-a':
        year, month = map(int, date.split('/'))
        weather_data = parser.parse_files_month_wise(year=year, month=month)
        weather_calculator = WeatherCalculator(weather_data)
        results = weather_calculator.calculate_monthly_averages(year, month)
        report = WeatherReport(results)
        output = report.generate_average_weather_yearly_report()
        print(output)
    elif command == '-c':
        year, month = map(int, date.split('/'))
        weather_data = parser.parse_files_month_wise(year=year, month=month)
        weather_calculator = WeatherCalculator(weather_data)
        results = weather_calculator.calculate_daily_temperatures(year, month)
        report = WeatherReport(results)
        output = report.generate_daily_temperatures_report(year, month)
        print(output)

    else:
        print("Invalid option:", command)
        sys.exit(1)


if __name__ == "__main__":
    main()
