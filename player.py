class Player:

    def __init__(self):
        self.resources = [0, 0, 0, 0, 100, 0, 0]
        self.resource_names = ["Credits", "Food", "Fuel", "Hull", "Stress Level", "Crew", "Wisdom"]
        # Resources: Credits, Food, Fuel, Hull, Stress, Crew, Wisdom

    def get_count(self):
        for x in range(0, 7):
            if x == 4:
                print(self.resource_names[x] + ": " + self.stress_status())
            else:
                print(self.resource_names[x] + ": " + str(self.resources[x]))

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
        if len(other) == 7:
            for x in range(0, 7):
                self.resources[x] += other[x]


p1 = Player()
p1.get_count()
myList = [100, 100, 100, 100, -80, 20, 20]
p1.add(myList)
p1.get_count()

            

