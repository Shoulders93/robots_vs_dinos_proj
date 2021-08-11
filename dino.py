class Dinosaurs:
    def __init__(self, name, health, attack_damage):
        self.name = name
        self.health = health
        self.attack_damage = attack_damage
    def attacking(self):
        self.attacking -= self.attack_damage