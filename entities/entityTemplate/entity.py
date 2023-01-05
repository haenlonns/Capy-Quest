# Samuel Bai
# 01/01/2023
# Contains general entity class, which serves as a constructor template for all game entities

class Entity:

    def __init__(self, name, maxhealth=1, attack=1, agility=1, critRate=0, critDMG=200) -> None:
        
        self.name = name
        self.maxhealth = maxhealth
        self.health = maxhealth # Entities start off at full health
        self.attack = attack
        self.agility = agility
        self.critRate = critRate
        self.critDMG = critDMG
