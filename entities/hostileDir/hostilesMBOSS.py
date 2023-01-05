# Sophia Deng
# 01/04/2023
# Constructor for Normal State Game Hostile Mini Boss Encounters

# Import from entityTemplate module
import sys
sys.path.append(r"Boomers-Game\entities")
from entityTemplate.entity import Entity

import random


# Sophia Deng
# 01/04/2023
# Constructor for Boar Encounter
class Boar:
    
    def __init__(self) -> None:
        health = 150
        attack = random.randint(100, 120)
        agility = 50

        self.stats = Entity(health, attack, agility)


# Sophia Deng
# 01/04/2023
# Constructor for Wolf Encounter
class Wolf:
    
    def __init__(self) -> None:
        health = 200
        attack = random.randint(150, 160)
        agility = 150
        crit = random.randint(15, 20)

        self.stats = Entity(health, attack, agility, crit)