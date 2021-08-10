from weapon import Weapon

class Robots:
    def __init__(self, name, health, weapon, attack_damage):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.attack_damage = attack_damage
    def attacking(self):
        self.attacking -= self.attack_damage