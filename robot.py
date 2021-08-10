from weapon import Weapon

class Robots:
    def __init__(self, name, health, weapon, attack_damage):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.attack_damage = attack_damage
    def attacking(self):
        self.attacking -= self.attack_damage

robot_one = Robots("Wallie", 100, "Sword", 15)
robot_two = Robots("Tinker", 100, "Lazer", 10)
robot_three = Robots("Rusty", 100, "Sword", 15)