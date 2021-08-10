class Weapon:
    def __init__(self, name, damage):
        self.weapon_type = name
        self.damage = damage

weapon_sword = Weapon("sword", 15)
weapon_lazer = Weapon("lazer", 10)