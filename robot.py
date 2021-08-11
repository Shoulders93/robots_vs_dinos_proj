from weapon import Weapon

class Robots:
    def __init__(self, name, health, attack_damage):
        self.name = name
        self.health = health
        # self.weapon = weapon
        self.attack_damage = attack_damage
    # def attacking(self):
    #     if self.health > 0:
    #         enemy.health -= self.attack_damage