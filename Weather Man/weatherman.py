# weatherman.py
from file_parser import WeatherParser
from weather_calculator import WeatherCalculator
from weather_reports import WeatherReport
import sys

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

    option_index = 0
    while option_index < len(options):
        option = options[option_index]
        if option == '-e':
            year = int(options[option_index + 1])
            results = calculator.calculate_yearly_extremes(year)
            report = WeatherReport(results)
            report.generate_extremes_report()
            option_index += 2
        elif option == '-a':
            year, month = map(int, options[option_index + 1].split('/'))
            results = calculator.calculate_monthly_averages(year, month)
            report = WeatherReport(results)
            report.generate_averages_report()
            option_index += 2
        elif option == '-c':
            year, month = map(int, options[i + 1].split('/'))
            results = calculator.calculate_daily_temperatures(year, month)
            report = WeatherReport(results)
            report.generate_daily_temperatures_report(year, month)
            option_index += 2
        else:
            print("Invalid option:", option)
            sys.exit(1)

if __name__ == "__main__":
    main()
