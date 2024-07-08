from constants import EXPECTED_NUMBER_OF_ARGS
import os
import sys


class InputParsing:
    def __init__(self, input_args):
        self.input_args = input_args

    def validate_args(self):
        """
        validate_args` function validates the command line arguments passed to the weatherman script.
        Args:
            self.input_args: List of command line arguments passed to the script.

        """
        message = ""
        if len(self.input_args) != EXPECTED_NUMBER_OF_ARGS:
            message = "Usage: weatherman.py /path/to/files-dir -e 2002 or -a 2002/3 or -c 2002/12"
            return False, message

        files_dir = self.input_args[0]
        if not os.path.isdir(files_dir):
            message = f"Error: {files_dir} is not a valid directory"
            return False, message

        command = self.input_args[1]
        date = self.input_args[2]
        if command == '-e':
            if not date.isdigit() or not (1996 <= int(date) <= 2011):
                message = "Error: Year must be between 1996 and 2011"
                return False, message
        elif command == '-a' or command == '-c':
            year_month = date.split('/')
            if len(year_month) != 2 or not (year_month[0].isdigit() and year_month[1].isdigit()):
                message = f"Error: Year/Month must be provided in YYYY/MM format after {command} option"
                return False,message
            year, month = int(year_month[0]), int(year_month[1])
            if not (1996 <= year <= 2011 and 1 <= month <= 12):
                message = "Error: Year must be between 1996 and 2011 and month must be between 1 and 12"
                return False, message

        else:
            message = f"Invalid option: {command}"
            return False, message

        return True, "validated"
