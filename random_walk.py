from random import choice


class RandomWalk:

    def __init__(self, num_points=5000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):

        # Iterate through a random walk while there are more points left
        while len(self.x_values) < self.num_points:

            # Decide which direction to go, and how far
            x_direction = choice([1, -1])
            x_distance = choice([x for x in range(0, 4)])
            x_step = x_distance * x_direction

            y_direction = choice([-1, 1])
            y_distance = choice([x for x in range(0, 4)])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            # Calc new pos (add last number in the array with the distance in x/y direction)
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
