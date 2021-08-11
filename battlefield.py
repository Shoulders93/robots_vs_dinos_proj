#Imports

from herd import Herd_of_dinosaurs
from fleet import Fleet_of_robots

class Battlefield:
    def __init__(self):
        self.team_dinosaurs = Herd_of_dinosaurs()
        self.team_robots = Fleet_of_robots()
    
    def battle_round(self, index):
        self.robots_attack = True
        self.dinosaurs_attack = True
        self.keep_fighting = True
        while self.keep_fighting:
            while self.dinosaurs_attack:
                if(self.team_robots.robot_fleet[index].health > 0):
                    self.team_robots.robot_fleet[index].health -= self.team_dinosaurs.dino_herd[index].attack_damage
                    print("Robot has " + str(self.team_robots.robot_fleet[index].health) + " health left!")
                    if(self.team_robots.robot_fleet[index].health <= 0):
                        print("Robot " + self.team_robots.robot_fleet[index].name + " has fainted!")
                        self.dinosaurs_attack = False
                        self.keep_fighting = False
                        self.robots_attack = False
                        break
                    if(self.dinosaurs_attack == True):
                        self.dinosaurs_attack = False
            while self.robots_attack:
                if(self.team_dinosaurs.dino_herd[index].health > 0):
                    self.team_dinosaurs.dino_herd[index].health -= self.team_robots.robot_fleet[index].attack_damage
                    print("Dinosaur has " + str(self.team_dinosaurs.dino_herd[index].health) + " health left!")
                    if(self.team_dinosaurs.dino_herd[index].health <= 0):
                        print("Dinosaur " + self.team_dinosaurs.dino_herd[index].name + " has fainted!")
                        self.dinosaurs_attack = False
                        self.keep_fighting = False
                        self.robots_attack = False
                        break
                    if(self.robots_attack == True):
                        self.robots_attack = False
            if(self.dinosaurs_attack == False and self.keep_fighting == True):
                    self.dinosaurs_attack = True
            if(self.robots_attack == False and self.keep_fighting == True):
                self.robots_attack = True