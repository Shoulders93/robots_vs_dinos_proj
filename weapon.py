class Weapon:
    def __init__(self, name):
        self.weapon_type = name
        self.damage = 0
    
    def specific_damage(self, damage):
        self.damage = damage
