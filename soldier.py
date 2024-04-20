import random

class Soldier:
    def __init__(self, health: int, strength: int):
        self.health = health
        self.strength = strength
        self.isAlive = True

    def attack(self):
        if self.isAlive:
            return self.strength


    def receiveDamage(self, damage):
        if not self.isAlive:
            return

        self.health -= damage
        
        if self.health <= 0:
            self.isAlive = False
            self.isAlive = False
            return

        self.health = self.health - damage


