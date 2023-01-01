# Samuel Bai
# 01/01/2023
# Constructor for Spider Enemy

from entity import Entity
import random


class Spider:

    def __init__(self) -> None:
        health = 30
        attack = random.randint(10, 15)

        self.entity = Entity(health, attack)

