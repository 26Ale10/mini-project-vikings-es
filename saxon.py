import random

from soldier import Soldier
# Aquí estuvo Alejandro


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
        print('Saxon created')

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        # self.damage = damage
        self.health = self.health - damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"
