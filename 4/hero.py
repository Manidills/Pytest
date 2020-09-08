from datetime import datetime


class hero:

    def __init__(self, name, date, power):
        self.name = name
        self.date = date
        self.power = power
        self.credits = 0

    def get_age(self):
        return (datetime.now() - self.dob).days // 365

    def add_movies(self, value):
        self.movies += value

    def get_movies(self):
        return self.movies
