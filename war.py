import random

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        if len(self.saxonArmy) == 0:
            print('No saxons alive be attacked')
            return
        if len(self.vikingArmy) == 0:
            print('No viking to attack')
            return

        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)

        saxon.receiveDamage(viking.strength)

        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
            return "A Saxon has died in combat"

    def saxonAttack(self):
        if len(self.vikingArmy) == 0:
            print('No vikings alive be attacked')
            return
        if len(self.saxonArmy) == 0:
            print('No saxon to attack')
            return

        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)

        msg = viking.receiveDamage(saxon.strength)

        if viking.health <= 0:
            self.vikingArmy.remove(viking)
            return
        return msg

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

    pass
