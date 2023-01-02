# Sophia Deng
# 01/01/2023
# Constructor for Snake Enemy

import sys
sys.path.append(r"Boomers-Game\entities")

from entityTemplate.entity import Entity
import random


class Snake:

    def __init__(self) -> None:
        health = 50
        attack = random.randint(20, 30)

        self.entity = Entity(health, attack)