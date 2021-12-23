
from characters.Character import Character
import Skills

class ShaktiMan(Character):
    
    def __init__(self):
        super().__init__()  
        self.skills = [Skills.FireBall(), Skills.ThunderBall(), Skills.SecretMantra()]