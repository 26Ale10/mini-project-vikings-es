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
        if self.health >= 0:
            print("Un 'Saxon' ha recibido PUNTOS DE DAÑO puntos de daño")
        else:
            print("Un 'Saxon' ha muerto en combate")
