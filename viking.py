
from soldier import Soldier


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
        print('Viking created')

    def attack(self):
        return self.strength

    def battleCry(self):
        return 'Odin Owns You All!'

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return f"{self.name} has died in act of combat"
        else:
            return f"{self.name} has received {damage} points of damage"
