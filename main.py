# MAIN: Controller/Initator of Application
# Author: Kory Attleson
# Create Date: August 10, 2021

# Imports:

from battlefield import Battlefield

# ** Instantiation of Objects

battle_one = Battlefield()
index = 0
while (index <= 2 ):
    battle_one.battle_round(index)
    index += 1
