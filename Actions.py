from characters.Character import Character


class Action():
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs

    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)


class MoveNorth(Action):
    def __init__(self):
        super().__init__(method=Character.moveNorth, name='Move north', hotkey='n')


class MoveSouth(Action):
    def __init__(self):
        super().__init__(method=Character.moveSouth, name='Move south', hotkey='s')


class MoveEast(Action):
    def __init__(self):
        super().__init__(method=Character.moveEast, name='Move east', hotkey='e')


class MoveWest(Action):
    def __init__(self):
        super().__init__(method=Character.moveWest, name='Move west', hotkey='w')


class ViewSkill(Action):
    """Prints the Character's skills"""

    def __init__(self):
        super().__init__(method=Character.displaySkills, name='View Skills', hotkey='i')


class Attack(Action):
    def __init__(self, enemy):
        super().__init__(method=Character.attack, name="Attack", hotkey='a', enemy=enemy)


class Escape(Action):
    def __init__(self, place):
        super().__init__(method=Character.escapeTo, name="Escape", hotkey='e', place=place)


class UsePassword(Action):
    def __init__(self):
        super().__init__(method=Character.use_password, name="Use Password", hotkey='u')
