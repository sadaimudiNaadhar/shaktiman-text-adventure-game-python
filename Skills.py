class Skill:
    # __init__ is the contructor method
    def __init__(self, name, description, damage, hotKey):
        self.name = name   # attribute of the Item class and any subclasses
        self.description = description  # attribute of the Item class and any subclasses
        self.damage = damage
        self.hotKey = hotKey

    # __str__ method is used to print the object

    def __str__(self):
        return "\n{}\n=====\n{}\nDamage: {}\n".format(self.name, self.description, self.damage)


class FireBall(Skill):
    def __init__(self):
        super().__init__("Fireball", "FireBall", 30, 'f')


class ThunderBall(Skill):
    def __init__(self):
        super().__init__("ThunderBall", "ThunderBall", 50, 't')


class SecretMantra(Skill):
    def __init__(self):
        super().__init__("SecretMantra", "SecretMantra", 60, 'm')
