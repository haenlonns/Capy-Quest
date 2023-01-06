# Sophia Deng
# 01/04/2023
# Constructor for Normal State Game Hostile Mini Boss Encounters

# Import from entityTemplate module
import sys
sys.path.append(r"Boomers-Game\combat\entities")
from entityTemplate.entity import Entity

import random


# Sophia Deng
# 01/04/2023
# Constructor for Boar Encounter
class Boar:
    
    def __init__(self) -> None:
        health = 300
        attack = random.randint(100, 120)
        agility = 10
        critRate = random.randint(10, 15)
        critDMG = random.randint(105, 110)

        self.stats = Entity(health, attack, agility, critRate, critDMG)


# Sophia Deng
# 01/04/2023
# Constructor for Wolf Encounter
class Wolf:
    
    def __init__(self) -> None:
        health = 200
        attack = random.randint(150, 160)
        agility = 30
        critRate = random.randint(15, 20)
        critDMG = random.randint(120, 125)

        self.stats = Entity(health, attack, agility, critRate, critDMG)