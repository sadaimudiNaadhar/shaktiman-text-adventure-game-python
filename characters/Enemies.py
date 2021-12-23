class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
 
    def isActive(self):
        return self.health > 0

class KillerJackal(Enemy):
    def __init__(self):
        super().__init__(name="Killer-Jackal", health=30, damage=50)
        
class ForestDog(Enemy):
    def __init__(self):
        super().__init__(name="ForestDog", health=20, damage=10)

class ForestWolf(Enemy):
    def __init__(self):
        super().__init__(name="ForestWolf", health=25, damage=15)
        
class TamrajKilvish(Enemy):
    def __init__(self):
        super().__init__(name="Tamraj Kilvish", health=100, damage=80)        