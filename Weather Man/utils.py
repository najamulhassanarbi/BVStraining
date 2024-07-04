
from constants import colors
import sys
import os


def validate_args(args):
    if len(args) < 2:
        print("Usage: weatherman.py /path/to/files-dir -e 2002 or -a 2002/03 or -c 2002/03")
        sys.exit(1)

    files_dir = args[0]
    if not os.path.isdir(files_dir):
        print(f"Error: {files_dir} is not a valid directory")
        sys.exit(1)

    options = args[1:]
    for index, option in enumerate(options):
        if option == '-e':
            if index + 1 >= len(options):
                print("Error: Year must be provided after -e option")
                sys.exit(1)
            year = options[index + 1]
            if not (year.isdigit() and 1996 <= int(year) <= 2011):
                print("Error: Year must be between 1996 and 2011")
                sys.exit(1)
        elif option == '-a' or option == '-c':
            if index + 1 >= len(options):
                print(f"Error: Year/Month must be provided in YYYY/MM format after {option} option")
                sys.exit(1)
            year_month = options[index + 1].split('/')
            if len(year_month) != 2 or not (year_month[0].isdigit() and year_month[1].isdigit()):
                print(f"Error: Year/Month must be provided in YYYY/MM format after {option} option")
                sys.exit(1)
            year, month = int(year_month[0]), int(year_month[1])
            if not (1996 <= year <= 2011 and 1 <= month <= 12):
                print("Error: Invalid year or month")
                sys.exit(1)

        else:
            print(f"Invalid option: {option}")
            sys.exit(1)


def print_colored_stars(num_stars, color):
    """
    Print colored stars to the console.
    Args:
    - num_stars: Number of stars to print.
    - color: Color of the stars.

    """
    for _ in range(int(num_stars)):
        color_print = colors[color]
        return f"{color_print}{'*' * int(num_stars)}\033[0m"

