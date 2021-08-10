from dino import Dinosaurs

class Herd_of_dinosaurs:
    def __init__(self):
        dino_one = Dinosaurs("T_rex", 100, 20)
        dino_two = Dinosaurs("Triceratops", 100, 12)
        dino_three = Dinosaurs("Velociraptor", 100, 8)
        self.dino_herd = [dino_one, dino_two, dino_three]