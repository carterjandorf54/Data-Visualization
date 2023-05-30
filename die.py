from random import randint


class Die:

    # Initialize an object with number of sides
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    # Return a random number from range 1 to num_sides
    def roll(self):
        return randint(1, self.num_sides)
