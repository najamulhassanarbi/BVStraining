"""
input_parsing.py

This module defines the InputParsing class, which parses and validates command line arguments for the weatherman script.

classes:
- InputParsing: A class to parse and validate command line arguments for the weatherman script.
"""


import os
import re

from collections import defaultdict

from constants import EXPECTED_NUMBER_OF_ARGS


class InputParsing:
    def __init__(self, input_args):
        """
        The constructor for InputParsing class.
        Args:
            input_args: List of command line arguments passed to the script.
        """

        self.input_args = defaultdict(str)
        self.input_args["python_file"] = input_args[0]
        self.input_args["files_dir"] = input_args[1]
        self.input_args["command"] = input_args[2]
        self.input_args["date"] = input_args[3]

    def validate_year(self, year):
        """
        The function validates the year.
        Args:
            year: The year to be validated.
        Returns:
            A tuple containing a boolean value indicating whether the year is valid, and a message explaining the result.
        """
        year_pattern = re.compile(r"^(199[6-9]|200[0-9]|2010|2011)$")
        if not year_pattern.match(year):
            message = "Error: Year must be between 1996 and 2011"
            return False, message

        return True, "Year is valid"

    def validate_date(self, date, command):
        """
        The function validates the date.
        Args:
            command: The command to be executed.
            date: The date to be validated.
        Returns:
            A tuple containing a boolean value indicating whether the date is valid, and a message explaining the result.
        """
        year_month_pattern = re.compile(r"^(199[6-9]|200[0-9]|2010|2011)/([1-9]|0[1-9]|1[0-2])$")
        if not year_month_pattern.match(date):
            message = f"Error: Year/Month must be provided in YYYY/MM format after {command} option"
            return False, message

        return True, "Date is valid"

    def validate_args(self):
        """
        This function validates the command line arguments passed to the weatherman script. Args:
        self.input_args:
            List of command line arguments passed to the script.
        Returns:
            A tuple containing a boolean value indicating whether the arguments are valid, a message explaining the result, and dictionary of input
        arguments.
        """
        message = ""
        if len(self.input_args) != EXPECTED_NUMBER_OF_ARGS:
            message = "Usage: weatherman.py /path/to/files-dir -e 2002 or -a 2002/3 or -c 2002/12"
            return False, message, self.input_args

        files_dir = self.input_args.get("files_dir")
        if not os.path.isdir(files_dir):
            message = f"Error: {files_dir} is not a valid directory"
            return False, message, self.input_args

        command = self.input_args.get("command")
        date = self.input_args.get("date")
        if command == '-e':
            is_valid, message = self.validate_year(date)
            if not is_valid:
                return False, message, self.input_args
        elif command == '-a' or command == '-c':
            is_valid, message = self.validate_date(date, command)
            if not is_valid:
                return False, message, self.input_args

        else:
            message = f"Invalid option: {command}"
            return False, message, self.input_args

        return True, "validated", self.input_args
