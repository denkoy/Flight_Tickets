import requests
from sensitive_data import SensitiveData


class UserSettings:
    def __init__(self):
        self.secret_data = SensitiveData()
        self.url = self.secret_data.sheety_link_users
        self.auth = self.secret_data.sheety_auth

    def add_row(self, first_name, last_name, email):

        json_to_add = {"user": {"firstName": first_name,
                                "surname": last_name,
                                "email": email}}
        response = requests.post(url=f"{self.url}", headers=self.auth, json=json_to_add)
        response.raise_for_status()

    def get_data(self):
        response_get = requests.get(url=self.url, headers=self.auth)
        response_get.raise_for_status()
        data = response_get.json()
        emails = []
        first_names = []
        last_names = []
        for i in data["users"]:
            first_names.append(i["firstName"])
            last_names.append(i["surname"])
            emails.append(i["email"])
        to_send = {'first_names': first_names, 'last_names': last_names, 'emails': emails}
        return to_send
