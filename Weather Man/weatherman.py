# weatherman.py

import sys
import os
from file_parser import WeatherParser
from weather_calculator import WeatherCalculator
from weather_reports import WeatherReport

def main():
    args = sys.argv[1:]
    if len(args) < 2:
        print("Usage: weatherman.py /path/to/files-dir -e 2002")
        sys.exit(1)
    
    files_dir = args[0]
    options = args[1:]

    parser = WeatherParser(files_dir)
    weather_data = parser.parse_files()
    calculator = WeatherCalculator(weather_data)

    i = 0
    while i < len(options):
        option = options[i]
        if option == '-e':
            year = int(options[i + 1])
            results = calculator.calculate_yearly_extremes(year)
            report = WeatherReport(results)
            report.generate_extremes_report()
            i += 2
        elif option == '-a':
            year, month = map(int, options[i + 1].split('/'))
            results = calculator.calculate_monthly_averages(year, month)
            report = WeatherReport(results)
            report.generate_averages_report()
            i += 2
        elif option == '-c':
            year, month = map(int, options[i + 1].split('/'))
            results = calculator.calculate_daily_temperatures(year, month)
            report = WeatherReport(results)
            report.generate_daily_temperatures_report(year, month)
            i += 2
        else:
            print("Invalid option:", option)
            sys.exit(1)

if __name__ == "__main__":
    main()
