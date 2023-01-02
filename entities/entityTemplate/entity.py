# Samuel Bai
# 01/01/2023
# Contains general entity class, which serves as a constructor template for all game entities

class Entity:

    def __init__(self, health=1, attack=1, agility=1) -> None:
        
        self.health = health
        self.attack = attack
        self.agility = agility
