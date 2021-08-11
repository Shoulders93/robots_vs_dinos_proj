#Imports

from herd import Herd_of_dinosaurs
from fleet import Fleet_of_robots

class Battlefield:
    def __init__(self):
        self.team_dinosaurs = Herd_of_dinosaurs
        self.team_robots = Fleet_of_robots
    
    def round_one(self):
        self.robots_attack = True
        self.dinosaurs_attack = True
        self.keep_fighting = True
        while self.keep_fighting:
            while self.dinosaurs_attack:
                if(Herd_of_dinosaurs.dino_herd[1].health > 0):
                    Fleet_of_robots.robot_fleet[1].health -= Herd_of_dinosaurs.dino_herd[1].attack_damage
                    print("Robot has" + Fleet_of_robots.robot_fleet[1].health + "left!")
                    self.dinosaurs_attack != self.dinosaurs_attack
                elif(Herd_of_dinosaurs.dino_herd[1].health == 0):
                    self.dinosaurs_attack = False
    
    def round_two(self, robots, dinosaurs):
        self.first_turn = robots
        self.second_turn = dinosaurs

    def round_three(self, robots, dinosaurs):
        self.first_turn = dinosaurs
        self.second_turn = robots