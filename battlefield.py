from herd import Herd_of_dinosaurs
from fleet import Fleet_of_robots

class Battlefield:
    def __init__(self):
        self.keep_fighting = True
    
    def time_to_fight(self):
        self.first_battle = Herd_of_dinosaurs[0]
        self.second_battle = Fleet_of_robots[0]