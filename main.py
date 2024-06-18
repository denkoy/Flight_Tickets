from data_manager import DataManager
from user_adder import UserSettings
import re


def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if re.match(email_regex, email):
        return True
    else:
        return False



y_or_no = input("Do you want to add new user, yes or no: ")
if y_or_no == "yes":
    first_name = input("Tell me your first name: ")
    last_name = input("Tell me your surname: ")
    email1 = input("Tell me your email: ")
    email2 = input("Confirm your email: ")
    if email1 == email2 and is_valid_email(email1):
        user_settings = UserSettings()
        user_settings.add_row(first_name, last_name, email1)
        program = DataManager()

else:
    program = DataManager()
    info=program.update_iatas()
    program.check_prices(info['iata_list'],info['fares'])

