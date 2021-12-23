
from characters.Character import Character
import Skills

class Geeta(Character):
    
    def __init__(self):
        super().__init__()  
        self.skills = [Skills.SecretMantra()]