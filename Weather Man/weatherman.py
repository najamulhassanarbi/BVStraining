# weatherman.py
from weather_parser import WeatherParser
from weather_calculator import WeatherCalculator
from weather_reports import WeatherReport
import sys
import os
import re


def main():
    args = sys.argv[1:]
    # validate_args(args)

    files_dir = args[0]
    options = args[1:]

    parser = WeatherParser(files_dir)

    option_index = 0
    while option_index < len(options):
        option = options[option_index]
        if option == '-e':
            year = int(options[option_index + 1])
            weather_data = parser.parse_files_year_wise(year)
            weather_calculator = WeatherCalculator(weather_data)
            results = weather_calculator.calculate_yearly_extremes(year)
            print(results)
            report = WeatherReport(results)
            output = report.generate_extremes_report()
            print(output)
            option_index += 2
        elif option == '-a':
            year, month = map(int, options[option_index + 1].split('/'))
            weather_data = parser.parse_files_month_wise(year=year, month=month)
            weather_calculator = WeatherCalculator(weather_data)
            results = weather_calculator.calculate_monthly_averages(year, month)
            report = WeatherReport(results)
            output = report.generate_averages_report()
            print(output)
            option_index += 2
        elif option == '-c':
            year, month = map(int, options[option_index + 1].split('/'))
            weather_data = parser.parse_files_month_wise(year=year, month=month)
            weather_calculator = WeatherCalculator(weather_data)
            results = weather_calculator.calculate_daily_temperatures(year, month)
            report = WeatherReport(results)
            output = report.generate_daily_temperatures_report(year, month)
            print(output)
            option_index += 2

        else:
            print("Invalid option:", option)
            sys.exit(1)


if __name__ == "__main__":
    main()
