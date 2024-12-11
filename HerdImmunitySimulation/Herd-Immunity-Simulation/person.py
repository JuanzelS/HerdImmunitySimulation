import random

class Person:
    def __init__(self, _id, is_vaccinated, infected=False):
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.infected = infected
        self.is_alive = True

    def did_survive_infection(self, mortality_rate):
        if random.random() < mortality_rate:
            self.is_alive = False
            self.infected = False
        else:
            self.is_vaccinated = True
            self.infected = False
        return self.is_alive
