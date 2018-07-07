# EncounterGroup keeps track of a group of encounters. It is able to store encounters,
# and retrieve random encounters.

import random


class encounterGroup:

    def __init__(self):
        self.encounters = []

    def add(self, encounter):
        self.encounters.append(encounter)

    def get_random_encounter(self):
        return random.choice(self.encounters)