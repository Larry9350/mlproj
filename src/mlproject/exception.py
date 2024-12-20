import sys
from src.mlproject.logger import logging  # Assuming logging is set up elsewhere in your project

def error_message_detail(error, error_detail: sys):
    # Using sys.exc_info() to get detailed information
    exc_type, exc_obj, exc_tb = sys.exc_info()  # This will provide the exception type, object, and traceback
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the file name where the error occurred
    error_message = "Error occurred in script: [{0}] at line number [{1}] with error message: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_details: sys):
        # Pass the error message to the base class
        super().__init__(error_message)
        # Now we handle the traceback separately
        self.error_message = error_message_detail(error_message, error_details)

    def __str__(self):
        return self.error_message
