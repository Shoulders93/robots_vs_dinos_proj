# MAIN: Controller/Initator of Application
# Author: Kory Attleson
# Create Date: August 10, 2021

# Imports:
from weapon import Weapon

lazer_weapon = Weapon("Lazer")
sword_weapon = Weapon("Sword")

lazer_weapon.specific_damage(10)
sword_weapon.specific_damage(15)