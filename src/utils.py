import sys

def error_message_detail(error,detail_error:sys):
    """
    Returns a detailed error message.
    
    Args:
        error (Exception): The exception to extract the message from.
        detail_error (sys): The sys module to access exc_info for traceback.
        
    Returns:
        str: A formatted string containing the error type and message.
    """
    _, _, exc_tb = detail_error.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    error_message="Error ocurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
        
        return error_message
         
    )
   
    class CustomException(Exception):
     def __init__(self, error_message, error_detail:sys):
        """
        Custom exception class to handle errors with detailed messages.
        
        Args:
            error_message (str): The error message to be displayed.
            error_detail (sys): The sys module to access exc_info for traceback.
        """
        super().__init__(error_message_detail(error_message, error_detail))
        self.error_message = error_message_detail(error_message, error_detai=error_detail)  

