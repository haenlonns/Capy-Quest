# Sophia Deng
# 01/01/2023
# Constructor for Normal State Game Hostile Encounters

# Import from entityTemplate module
import sys
sys.path.append(r"Boomers-Game\combat\entities")
from entityTemplate.entity import Entity

import random


# Sophia Deng
# 01/04/2023
# Constructor for Fox Encounter
class Fox:
    
    def __init__(self) -> None:
        health = 80
        attack = random.randint(60, 70)
        agility = 35
        critRate = random.randint(10, 15)
        critDMG = random.randint(120, 125)

        self.stats = Entity(health, attack, agility, critRate, critDMG)


# Sophia Deng
# 01/04/2023
# Constructor for Hawk Encounter
class Hawk:
    
    def __init__(self) -> None:
        health = 100
        attack = random.randint(70, 80)
        agility = 30
        critRate = random.randint(5, 10)
        critDMG = random.randint(105, 110)

        self.stats = Entity(health, attack, agility, critRate, critDMG)


# Sophia Deng
# 01/01/2023
# Constructor for Snake Encounter
class Snake:
    
    def __init__(self) -> None:
        health = 50
        attack = random.randint(20, 30)
        agility = 20

        self.stats = Entity(health, attack, agility)


# Samuel Bai
# 01/01/2023
# Constructor for Spider Encounter
class Spider:

    def __init__(self) -> None:
        health = 30
        attack = random.randint(10, 15)
        agility = 10

        self.stats = Entity(health, attack, agility)
