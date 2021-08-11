from dino import Dinosaurs

class Herd_of_dinosaurs:
    def __init__(self):
        self.dino_one = Dinosaurs("T_rex", 100, 20)
        self.dino_two = Dinosaurs("Triceratops", 100, 12)
        self.dino_three = Dinosaurs("Velociraptor", 100, 8)
        
    def dino_herd (self):
        self.dino_herd = [self.dino_one, self.dino_two, self.dino_three]