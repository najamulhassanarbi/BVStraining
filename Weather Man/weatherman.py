"""
weatherman.py

This module is the main entry point for the WeatherMan application

Usage:
- python weatherman.py <files_dir> <options>

"""
import sys

from output import OutputResults


def main():
    output = OutputResults(sys.argv)
    message = output.output()
    if message:
        print(message)


if __name__ == "__main__":
    main()
