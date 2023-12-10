import re

class Emailer:
    def __init__(self): ...

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """
                Checks if the provided email address is valid
                Args:
                    email(str): The email address
                Returns:
                    True if the provided email address is valid, False otherwise
                """
        # compilation error
        # email_regex = r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$'
        # doesn't pass test_is_valid_email_with_plus_number
        # email_regex = r'^[a-zA-Z0-9-.]+@([\w-]+\.)+[\w-]{2,4}$'
        email_regex = r'^[a-zA-Z0-9_.+-]+@([\w-]+\.)+[\w-]{2,4}$'

        return bool(re.match(email_regex, email))
