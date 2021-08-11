from robot import Robots

class Fleet_of_robots:
    def __init__(self):
        robot_one = Robots("Wallie", 100, 15)
        robot_two = Robots("Tinker", 100, 10)
        robot_three = Robots("Rusty", 100, 15)
        self.robot_fleet = [robot_one, robot_two, robot_three]