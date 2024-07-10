"""
input_parsing.py

This module defines the InputParsing class, which parses and validates command line arguments for the weatherman script.

classes:
- InputParsing: A class to parse and validate command line arguments for the weatherman script.
"""

import os
import re

from collections import defaultdict

from constants import EXPECTED_NUMBER_OF_ARGS, MESSAGES


class InputParsing:
    def __init__(self, input_args):
        """
        The constructor for InputParsing class.
        Args:
            input_args: List of command line arguments passed to the script.
        """

        self.input_args = input_args

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
            message = MESSAGES.get("error_for_year")
            return False, message

        return True, MESSAGES.get("valid")

    def validate_date(self, date):
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
            message = MESSAGES.get("error_for_date")
            return False, message

        return True, MESSAGES.get("valid")

    def validate_file(self, input_arguments):
        """
        The function validates the date.
        Args:
            input_arguments: The command to be executed.
            input_arguments: The date to be validated.
        Returns:
            A tuple containing a boolean value indicating whether the date is valid, and a message explaining the result.
        """

        files_dir = input_arguments.get("files_dir")
        if not os.path.isdir(files_dir):
            message = MESSAGES.get("file_error")
            return False, message
        return True, MESSAGES.get("valid")

    def validate_commands(self, input_arguments):
        """
        This function validates the command line arguments passed to the weatherman script.
        self.input_args:
            List of command line arguments passed to the script.
        Returns:
            A tuple containing a boolean value indicating whether the arguments are valid, a message explaining the result, and dictionary of input
        arguments.
        """

        command = input_arguments.get("command")
        date = input_arguments.get("date")
        if command == '-e':
            is_valid, message = self.validate_year(date)
            if not is_valid:
                return False, message
        elif command == '-a' or command == '-c':

            is_valid, message = self.validate_date(date)
            if not is_valid:
                return False, message

        else:
            message = MESSAGES.get("invalid")
            return False, message

        return True, MESSAGES.get("valid")

    def validate_args(self):
        """
        This function validates the command line arguments passed to the weatherman script.
        Args: elf.input_args:
            List of command line arguments passed to the script. Returns: A tuple containing a boolean value indicating
            whether the arguments are valid, a message explaining the result, and dictionary of input arguments.
        """
        if len(self.input_args) < EXPECTED_NUMBER_OF_ARGS:
            message = MESSAGES.get("usage")
            return False, message, self.input_args

        input_arguments = defaultdict(str)
        input_arguments["python_file"] = self.input_args[0]
        input_arguments["files_dir"] = self.input_args[1]
        input_arguments["command"] = self.input_args[2]
        input_arguments["date"] = self.input_args[3]

        file_is_valid, message = self.validate_file(input_arguments)
        if not file_is_valid:
            return False, message, input_arguments

        command_date_valid, message = self.validate_commands(input_arguments)

        if not command_date_valid:
            return False, message, input_arguments

        return True, MESSAGES.get("valid"), input_arguments
