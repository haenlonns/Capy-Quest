# Samuel Bai
# 01/02/2023
# Controls Game State

import random


class gameController:

    def __init__(self) -> None:
        
        self.stage = 0 # initialize from gameData file
        self.level = 1 # initialize from gameData file
    
    # Samuel Bai
    # 01/02/2023
    # Controls type of game event generated based on GAME LEVEL
    def createEvent(self):

        if self.level == 10:
            self.runBossEvent
            self.stage += 1
            self.level = 0
        
        else:
            self.runLevelEvent
            self.level += 1
    
    # Samuel Bai
    # 01/02/2023
    # Generates boss event based on GAME STAGE
    def runBossEvent(self):
        # Fight Boss
        pass

    # Samuel Bai
    # 01/02/2023
    # Generates game event based on GAME LEVEL & GAME STAGE
    def runLevelEvent(self):
        
        eventPicker = random.randint(1, 100)

        if self.level == 1:
            # compare eventPicker to list of possible event (dict)
            pass
