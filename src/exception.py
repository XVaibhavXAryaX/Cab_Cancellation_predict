import sys
import logging
import traceback


def error_message_detail(error, exc_tb):
    """
    Returns a detailed error message using traceback info.

    Args:
        error (Exception): The exception to extract the message from.
        exc_tb (traceback object): traceback object from sys.exc_info()[2]

    Returns:
        str: A formatted string containing the error type and message.
    """
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    return "Error occurred in python script [{0}] line number [{1}] error message [{2}]".format(
        file_name, line_number, str(error)
    )


class CustomException(Exception):
    def __init__(self, error_message, exc_tb):
        """
        Custom exception class to handle errors with detailed messages.

        Args:
            error_message (str): The error message to be displayed.
            exc_tb (traceback): traceback object from sys.exc_info()[2]
        """
        super().__init__(error_message_detail(error_message, exc_tb))
        self.error_message = error_message_detail(error_message, exc_tb)

    def __str__(self):
        return self.error_message


