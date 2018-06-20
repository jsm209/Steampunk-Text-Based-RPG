class Player:

    #############
    # CONSTANTS #
    #############

    # This is terrible but the gender is assumed to be male! Maybe I'll implement a female player later on.
    # Favors younger, taller, medium weight males.
    OPTIMUM_AGE = 30  # in years
    OPTIMUM_HEIGHT = 183  # in cm
    OPTIMUM_WEIGHT = 70  # in kg

    # Pre: Given a name, a height in cm, a weight in kg, and a height in years,
    # Post: Will construct a character that has attributes based on given values.
    def __init__(self, name, height, weight, age):
        self.stats = {
                      "Name": name,
                      "Height": height,
                      "Weight": weight,
                      "Age": age,
                      "Hunger": round((weight/self.OPTIMUM_WEIGHT) * 100),
                      "HP": round(100 - abs(self.OPTIMUM_AGE-age)),
                      "ATK": round((height/self.OPTIMUM_HEIGHT) * 100),
                      "DEF": 0,
                      "Inventory": []
        }

    def __str__(self):
        total = ""
        for x in self.stats:
            total = total + x + ": " + str(self.stats[x]) + "\n"
        return total


p1 = Player("Joshua", 180, 58, 19)
print(str(p1))

p2 = Player("Wario", 170, 140, 18)
print(str(p2))

p1 = Player("Toad", 100, 35, 5)
print(str(p1))

            

