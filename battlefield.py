#Imports

from herd import Herd_of_dinosaurs
from fleet import Fleet_of_robots

class Battlefield:
    def __init__(self):
        self.team_dinosaurs = Herd_of_dinosaurs()
        self.team_robots = Fleet_of_robots()
    
    def round_one(self):
        self.robots_attack = True
        self.dinosaurs_attack = True
        self.keep_fighting = True
        while self.keep_fighting:
            while self.dinosaurs_attack:
                if(self.team_robots.robot_one.health > 0):
                    self.team_robots.robot_one.health -= self.team_dinosaurs.dino_one.attack_damage
                    print("Robot has " + str(self.team_robots.robot_one.health) + " left!")
                    if(self.team_robots.robot_one.health == 0):
                        print("Robot has fainted!")
                        self.dinosaurs_attack = False
                        self.keep_fighting = False
                        self.robots_attack = False
                        break
                    if(self.dinosaurs_attack == True):
                        self.dinosaurs_attack = False
                # elif(self.team_robots.robot_one.health == 0):
                #     print("Robot has fainted!")
                #     self.dinosaurs_attack = False
                #     self.keep_fighting = False
            while self.robots_attack:
                if(self.team_dinosaurs.dino_one.health > 0):
                    self.team_dinosaurs.dino_one.health -= self.team_robots.robot_one.attack_damage
                    print("Dinosaur has " + str(self.team_dinosaurs.dino_one.health) + " left!")
                    if(self.robots_attack == True):
                        self.robots_attack = False
                    else:
                        self.robots_attack = True
                elif(self.team_dinosaurs.dino_one.health == 0):
                    print("Dinosaur has fainted!")
                    self.robots_attack = False
            if(self.dinosaurs_attack == False and self.keep_fighting == True):
                    self.dinosaurs_attack = True
            if(self.robots_attack == False and self.keep_fighting == True):
                self.robots_attack = True

    def next_turn(self):
        if (self.dinosaurs_attack == True):
            self.dinosaurs_attack = False
        else:
            self.dinosaurs_attack = True
    
    def next_turn1(self):
        if (self.robots_attack == True):
            self.robots_attack = False
        else:
            self.robots_attack = True

    # def round_two(self, robots, dinosaurs):

    # def round_three(self, robots, dinosaurs):
