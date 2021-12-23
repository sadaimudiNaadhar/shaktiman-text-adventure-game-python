from PlanetX import PlanetX
from characters.Geeta import Geeta
from characters.ShaktiMan import ShaktiMan
import Levels
import StoryLine


class Main:

    def __init__(self) -> None:
        print(StoryLine.introLogo)

    def play(self) -> None:
        levels = [Levels.Level1(), Levels.Level2(), Levels.Level3()]

        for level in levels:
            level.loadMap()
            print("\n", level.getIntro())

            if isinstance(level, Levels.Level1) or isinstance(level, Levels.Level2):
                player = ShaktiMan()
            else:
                print("\n1. Shaktiman")
                print("\n2. Geeta")
                while True:
                    chInp = input("\n Choose a character: ")
                    if(chInp == '1'):
                        player = ShaktiMan()
                        break
                    if(chInp == '2'):
                        player = Geeta()
                        break

                print("\nYou choosed character ", player.getCharacterName())

            player.victory = False
            player.setPosition(0, 0)

            while player.isActive() and not player.victory:
                place = PlanetX.getPlace(player.get_X(), player.get_Y())

                place.setupEnvironment(player)

                if player.isActive() and not player.victory:
                    print("\nChoose an action:\n")

                    availableActions = place.getActions()
                    for action in availableActions:
                        print(action)

                    actionInput = input('\nAction: ')

                    for action in availableActions:
                        if actionInput == action.hotkey:
                            player.doAction(action, **action.kwargs)
                            break


if __name__ == "__main__":
    Main().play()
