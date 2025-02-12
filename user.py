import random
import string
import re
from datetime import datetime


class User:
    def __init__(self, user_id, name, surname, birthday):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.email = UserUtil.generate_email(name, surname, "example.com")
        self.password = UserUtil.generate_password()
        self.birthday = birthday

    def get_details(self):
        return f"ID: {self.user_id}, Name: {self.name} {self.surname}, Email: {self.email}, Birthday: {self.birthday.strftime('%Y-%m-%d')}"

    def get_age(self):
        today = datetime.today()
        return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))


