from playsound import playsound
import Places
import PlanetX as PX
import Skills
import characters.Enemies as Enemies
import random 
import SoundStore

class Character():
    def __init__(self):

        self.health = 100
        self.victory = False #no victory on start up
        
    def getCharacterName(self):
        return type(self).__name__ 
        
    def setPosition(self, x, y):
        self.location_x = x
        self.location_y = y
        
    def get_X(self):
        return self.location_x
        
    def get_Y(self):
        return self.location_y  
            
    # isActive method
    def isActive(self):
        return self.health > 0   #Greater than zero value then you are still alive
 
    def displaySkills(self):
        for item in self.skills:
            print(item, '\n')
    
    def move(self, dx, dy):
        
        self.location_x += dx
        self.location_y += dy
        
    def moveNorth(self):
        self.move(dx=0, dy=-1)
 
    def moveSouth(self):
        self.move(dx=0, dy=1)
 
    def moveEast(self):
        self.move(dx=1, dy=0)
 
    def moveWest(self):
        self.move(dx=-1, dy=0)

    def attack(self, enemy):
        
        for i in self.skills:
         if isinstance(i, Skills.Skill):
             print(i.hotKey, ":", i.name)

        skill = input("\n Choose a Skill: ")
        
        for i in self.skills:
         if isinstance(i, Skills.Skill):
             if(skill == i.hotKey):
                 usedSkill = i
        
        print("You use {} against {}!".format(usedSkill.name, enemy.name))
        
        if isinstance(enemy, Enemies.KillerJackal):
            if not isinstance(usedSkill, Skills.FireBall):
                self.health -= enemy.damage
                print("You used wrong skill, you are attacked by {}!".format(enemy.name))
                print("Your Health {}!".format(self.health))
        
            else:
                playsound(SoundStore.punch_sound)
                enemy.health -= usedSkill.damage
                
        if isinstance(enemy, Enemies.TamrajKilvish):
            if not isinstance(usedSkill, Skills.SecretMantra):
                self.health -= enemy.damage
                print("You used wrong skill, you are attacked by {}!".format(enemy.name))
                print("Your Health {}!".format(self.name))
        
            else:
                enemy.health = 0        
                
        if isinstance(enemy, Enemies.ForestDog) or isinstance(enemy, Enemies.ForestWolf):
            playsound(SoundStore.punch_sound)
            enemy.health -= usedSkill.damage          
        
        if not enemy.isActive():
            print("You killed {}!".format(enemy.name))
            #playsound("sounds/spell.mp3")
        else:
            print("Remaining Health for {} is {}.".format(enemy.name, enemy.health))
            
        if (self.health <= 0):
            print("Character died! Game Over")

    def doAction(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
                    action_method(**kwargs)
                
    def escapeTo(self, place):
        """Moves the player randomly to an adjacent place"""
        available_moves = place.getDirections()
        r = random.randint(0, len(available_moves) - 1)
        self.doAction(available_moves[r])                  
        
    def use_password(self):
        Places.Place.passwordUsed = True
            