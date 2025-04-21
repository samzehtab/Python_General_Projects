# In the name of God
# Mohammad Hossein Zehtab
# Advanced-Python-Wednesdays
# Regex: Valid_phone_number

import re

def is_valid_phone_number(phone_number : str):
    """
    Checking if a phone number is valid or not.
    """
    # pattern = r"\+\d+(([ -.]\d+){3}|( \(\d{3}\) \d+))?"
    pattern = r"^(\+\d{1,3})?[\s.-]?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}$"
    
    result = re.fullmatch(pattern=pattern, string=phone_number)
    print("Valid") if result else print("Not Valid")

### Driver Code ###
is_valid_phone_number("+98.912.717.5477")
is_valid_phone_number("+98 912 717 5477")
is_valid_phone_number("+98-912-717-5477")
is_valid_phone_number("+989127175477")
is_valid_phone_number("+98 (912) 7175477")
print()
is_valid_phone_number("98 912 717 5477")
is_valid_phone_number("+98912717")
is_valid_phone_number("+98 912 p17 5477")
is_valid_phone_number("+44 (0) 20 234 5678")