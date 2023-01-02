# Sophia Deng
# 01/01/2023
# Constructor for Normal State Game Hostile Encounters

# Import from entityTemplate module
import sys
sys.path.append(r"Boomers-Game\entities")
from entityTemplate.entity import Entity

import random


# Sophia Deng
# 01/01/2023
# Constructor for Snake Encounter
class Snake:
    
    def __init__(self) -> None:
        health = 50
        attack = random.randint(20, 30)

        self.stats = Entity(health, attack)


# Samuel Bai
# 01/01/2023
# Constructor for Spider Encounter
class Spider:

    def __init__(self) -> None:
        health = 30
        attack = random.randint(10, 15)

        self.stats = Entity(health, attack)
