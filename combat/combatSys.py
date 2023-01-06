# Samuel Bai
# 01/06/2023
# Handles game combat

import random
import entities.hostileDir
import entities.playerDir


class combatSys:

    def __init__(self, hostileEntity, playerEntity) -> None:
        self.hostileEntity = hostileEntity
        self.player = playerEntity

    def handleCombat(self):
        
        while (self.player.stats.health > 0) and (self.hostileEntity.stats.health > 0):
            self.handleTurn
        
        return self.player

    def handleTurn(self):

        if not (self.checkDodge(self.player)):
            self.calcPDamage()
        
        if not (self.checkDodge(self.hostileEntity)):
            self.calcEDamage()

    def calcPDamage(self, modifiers=0):
        
        modifiedDMG = self.hostileEntity.stats.attack # - player items
        if self.checkCrit(self.hostileEntity):
            modifiedDMG = modifiedDMG * (self.hostileEntity.stats.critDMG / 100)

        self.player.stats.health = self.player.stats.health - modifiedDMG

    def calcEDamage(self, modifiers=0):

        modifiedATK = self.player.stats.attack # + player items
        if self.checkCrit(self.player):
            modifiedATK = modifiedATK * (self.player.stats.critDMG / 100)

        self.hostileEntity.stats.health = self.hostileEntity.stats.health - modifiedATK
    
    def checkDodge(self, entity):
        
        dodgeVal = random.randint(1, 100)
        dodgeBool = entity.stats.agility >= dodgeVal

        return dodgeBool    

    def checkCrit(self, entity):

        critVal = random.randint(1, 100)
        critBool = entity.stats.critRate >= critVal

        return critBool
        
