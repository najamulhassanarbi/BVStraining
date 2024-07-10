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
    output.output()


if __name__ == "__main__":
    main()
