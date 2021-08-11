from robot import Robots

class Fleet_of_robots:
    def __init__(self):
        self.robot_one = Robots("Wallie", 100, 15)
        self.robot_two = Robots("Tinker", 100, 10)
        self.robot_three = Robots("Rusty", 100, 15)
        self.robot_fleet = [self.robot_one, self.robot_two, self.robot_three]