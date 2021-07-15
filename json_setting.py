import json


class JsonSetting:
    def __init__(self, users_filename):
        self.filename = users_filename
        self.users = self.read_user_list()

    def read_user_list(self):
        filename = 'users.json'
        with open(filename, 'r') as json_file:
            udict = json.load(json_file)
        return udict

    def write_user_list(self, user):
        filename = 'users.json'
        with open(filename, 'w') as json_file:
            self.users.append(user)
            json.dump(self.users, json_file)
