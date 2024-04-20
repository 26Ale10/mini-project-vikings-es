import random

class War2():
    def __init__(self, one, two):
        seed = random.randint(0, 1)
        if seed == 0:
            self.vikingCommander = one
            self.saxonCommander = two
        else:
            self.vikingCommander = two
            self.saxonCommander = one

        print("Vikings lead by %s" % self.vikingCommander)
        print("Saxons lead by %s" % self.saxonCommander)

        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        if len(self.saxonArmy) == 0:
            print("No saxons from %s alive be attacked" % self.saxonCommander)
            return
        if len(self.vikingArmy) == 0:
            print("No viking from %s to attack" % self.vikingCommander)
            return

        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)

        saxon.receiveDamage(viking.strength)

        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
            return "A Saxon of %s has died in combat" % self.saxonCommander

    def saxonAttack(self):
        if len(self.vikingArmy) == 0:
            print("No vikings from %s alive be attacked" % self.vikingCommander)
            return
        if len(self.saxonArmy) == 0:
            print("No saxon from %s to attack" % self.saxonCommander)
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
            return "Vikings of %s have won the war of the century!" % self.vikingCommander
        elif len(self.vikingArmy) == 0:
            return "Saxons of %s have fought for their lives and survive another day..." % self.saxonCommander
        else:
            return "Vikings of %s and Saxons of %s are still in the thick of battle." % (self.vikingCommander, self.saxonCommander)

    pass

