# Samuel Bai
# 01/02/2023
# Constructor for Player Entity

# Import from entityTemplate module
import sys
sys.path.append(r"Boomers-Game\combat\entities")
from entityTemplate.entity import Entity


class Player:

    def __init__(self) -> None:
        
        self.inventory = []
        self.experience = 0
        self.level = 1
        self.gold = 0

        health = 100
        self.stats = Entity(*self.getStats())

    # Samuel Bai
    # 01/02/2023
    # Prompt user to distribute stat points amongst MODifiable stats
    def getStats(self):
        pass

        