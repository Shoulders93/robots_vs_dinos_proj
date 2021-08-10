class Dinosaurs:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_damage = attack_power
    def attacking(self):
        self.attacking -= self.attack_damage

dino_one = Dinosaurs("T_rex", 100, 20)
dino_two = Dinosaurs("Triceratops", 100, 12)
dino_three = Dinosaurs("Velociraptor", 100, 8)