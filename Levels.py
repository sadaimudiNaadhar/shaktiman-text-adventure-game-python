from PlanetX import PlanetX
from playsound import playsound
import SoundStore
import StoryLine


class Level1(PlanetX):
    def __init__(self) -> None:
        super().__init__(routeMap='maps/level1_map.txt')

    def getIntro(self):
        playsound(SoundStore.shaktiManIntro)
        playsound(SoundStore.level1)
        playsound(SoundStore.level1_intro, False)

        return StoryLine.level1Intro


class Level2(PlanetX):
    def __init__(self) -> None:
        super().__init__(routeMap='maps/level2_map.txt')

    def getIntro(self):
        playsound(SoundStore.level2)
        playsound(SoundStore.level2_intro, False)

        return StoryLine.level2Intro


class Level3(PlanetX):
    def __init__(self) -> None:
        super().__init__(routeMap='maps/level3_map.txt')

    def getIntro(self):
        playsound(SoundStore.level3)
        playsound(SoundStore.level3_intro, False)
        
        return StoryLine.level3Intro
