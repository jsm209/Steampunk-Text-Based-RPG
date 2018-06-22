class Player:



    def __init__(self):
        self.resources = [0, 0, 0, 0, 100, 0, 0]
        self.resource_names = ["Credits", "Food", "Fuel", "Hull", "Stress Level", "Crew", "Wisdom"]
        # Resources: Credits, Food, Fuel, Hull, Stress, Crew, Wisdom


    def get_count(self):
        for x in self.resource_names:
            print(x + ": " + str(self.resources[x]))

    def stress_status(self):
        if self.resources[4] <= 20:
            return "Almost insane"
        elif self.resources[4] <= 40:
            return "Dangerously stressed"
        elif self.resources[4] <= 60:
            return "Acutely stressed"
        elif self.resources[4] <= 80:
            return "Moderately stressed"
        else:
            return "Nervous"


    def add(self, other):
        if other.len() == 7:
            for x in other:
                self.resources[x] += x




p1 = Player()
p1.get_count()
p1.add([100, 100, 100, 100, -80, 20, 20])
p1.get_count()

            

