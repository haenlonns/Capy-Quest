# Samuel Bai
# 01/01/2023
# Contains general entity class, which serves as a constructor template for all game entities

class Entity:

    def __init__(self, health, attack) -> None:
        
        self.health = health
        self.attack = attack
