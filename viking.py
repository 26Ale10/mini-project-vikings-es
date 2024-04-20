
from soldier import Soldier

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
        print('Viking created')

    def attack() ->str:
        return "Odin Owns You All!"
    
    def battleCry(self) -> str:
        return '¡Odin os posee a todos!'

    def receiveDamage(self, damage) -> str:
        self.health -= damage
        if self.health <= 0:
            return f"{self.name} ha muerto en acto de combate"
        else:
            return f"{self.name} ha recibido PUNTOS DE DAÑO"
