
import Actions
import PlanetX as PX
import characters.Enemies as Enemies
import StoryLine
from playsound import playsound
import SoundStore


class Place:

    placeUnlocked = False
    passwordUsed = False

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def setupEnvironment(self, player):
        raise NotImplementedError()

    def getIntro(self):
        raise NotImplementedError()

    def getDirections(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if PX.PlanetX.getPlace(self.x + 1, self.y):
            moves.append(Actions.MoveEast())
        if PX.PlanetX.getPlace(self.x - 1, self.y):
            moves.append(Actions.MoveWest())
        if PX.PlanetX.getPlace(self.x, self.y - 1):
            moves.append(Actions.MoveNorth())
        if PX.PlanetX.getPlace(self.x, self.y + 1):
            moves.append(Actions.MoveSouth())
        return moves

    def getActions(self):
        """Returns all of the available actions in this room."""
        actions = self.getDirections()
        actions.append(Actions.ViewSkill())

        return actions


class EnemyPlace(Place):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def setupEnvironment(self, player):
        if self.enemy.isActive():
            player.health = player.health - self.enemy.damage
            print("Enemy does {} damage. You have {} health remaining.".format(
                self.enemy.damage, player.health))

    def getActions(self):
        if self.enemy.isActive():
            return [Actions.Attack(enemy=self.enemy), Actions.Escape(place=self)]
        else:
            return self.getDirections()


class StoryBegin(Place):
    def getIntro(self):
        return """
        The Shaktiman
        """

    def setupEnvironment(self, player):
        pass


class MeetingJackal(EnemyPlace):

    def __init__(self, x, y):
        super().__init__(x, y, Enemies.KillerJackal())

    def setupEnvironment(self, player):
        if not self.enemy.isActive():
            print(StoryLine.jackalStoryEnd)
            clue = None
            while clue != 'something':
                clue = input(
                    "Type something to unlock the clue from " + self.enemy.name + ": ")
                if(clue == 'something'):
                    Place.placeUnlocked = True
                    print(StoryLine.GeetaClue)
                else:
                    print("Sorry wrong input! Try ")

        else:
            print(self.getIntro())

    def getIntro(self):
        return StoryLine.jackalStory


class GetAdvice(Place):

    def setupEnvironment(self, player):
        self.getIntro()

    def getIntro(self):
        return """
        Advice: Play wisely!
        """


class GeetaPasswordSpot(Place):

    def setupEnvironment(self, player):
        if not Place.placeUnlocked:
            return print(StoryLine.NotUnlocked)
        else:
            print("Note down this password: ", StoryLine.GeetaPassword)

        input("Press any key to collect this password! ")

        playsound(SoundStore.level1_completed)
        # Pass to level 2
        player.victory = True

    def getIntro(self):
        return """
        The GeetaPasswordSpot
        """


class RechargeHealth(Place):

    def setupEnvironment(self, player):
        self.getIntro()
        if(player.health < 100):
            player.health = 100

        print("Shaktimans Health Recharged Successfully!")

    def getIntro(self):
        return """
        The RechargeHealth Room
        """


class Unknown(Place):

    def setupEnvironment(self, player):
        print(self.getIntro())

    def getIntro(self):
        return """
        The Unknown Shades!!!!
        """


class DeepForest(Place):

    def setupEnvironment(self, player):
        print(self.getIntro())

    def getIntro(self):
        return """
        Your are inside a Deep Poisounous Forest! For each move you loose 10 Health points
        Hint: You can make use of Health Reacharge Room
        """


class GeetaPlace(Place):

    def setupEnvironment(self, player):

        if not self.passwordUsed:
            return print(self.getIntro())

        playsound(SoundStore.geeta_saved, False)

        input("You have successfully saved Geeta! Press any key to start next level ")
        # Pass to level 3
        player.victory = True

    def getActions(self):
        """Returns all of the available actions in this room."""
        actions = self.getDirections()
        actions.append(Actions.UsePassword())

        return actions

    def getIntro(self):
        return """
        Secret Room
        Hint: You can make use of the collected Password Here!
        """


class PoisonousPlace(Place):

    def setupEnvironment(self, player):
        print(self.getIntro())
        playsound(SoundStore.cough, False)
        player.health -= 10

        print("Health reduced to : ", player.health)

    def getIntro(self):
        return """
        Your are inside a Deep Poisounous Forest!
        Hint: You can make use of Health Reacharge Room
        """


class FinalStart(Place):
    def getIntro(self):
        return """
        Mission kill kilvish
        """

    def setupEnvironment(self, player):
        print(self.getIntro())


class KilvishPlace(EnemyPlace):

    def __init__(self, x, y):
        super().__init__(x, y, Enemies.TamrajKilvish())

    def setupEnvironment(self, player):
        if self.enemy.isActive():
            print(self.getIntro())

            super().setupEnvironment(player)
        else:
           
            print("Game won!")
            player.victory = True
            playsound(SoundStore.game_won)

    def getIntro(self):
        return """
        Your are now attacking by Creepy Kilvish!
        Hint: You need to make use of your mantra!
        """


class WolfPlace(EnemyPlace):

    def __init__(self, x, y):
        super().__init__(x, y, Enemies.ForestWolf())

    def setupEnvironment(self, player):
        if self.enemy.isActive():
            print(player.getCharacterName(), self.getIntro())
            super().setupEnvironment(player)
        else:
            return print("Rotten smell of wolf!")

    def getIntro(self):
        return " is attacked by a Wolf!"


class DogPlace(EnemyPlace):

    def __init__(self, x, y):
        super().__init__(x, y, Enemies.ForestDog())

    def setupEnvironment(self, player):
        if self.enemy.isActive():
            print(player.getCharacterName(), self.getIntro())
            super().setupEnvironment(player)
        else:
            return print("Rotten smell of Dog!")

    def getIntro(self):
        return " is attacked by a Dog!"
