
from Places import Unknown


class PlanetX:

    startPosition = (0, 0)
    world = {}

    def __init__(self, routeMap) -> None:
        self.routeMap = routeMap

    # load the map
    def loadMap(self):
        """Parses a file that describes the world space into the _world object"""
        with open(self.routeMap, 'r') as f:
            rows = f.readlines()

        if len(rows) <= 0:
            return

        for y in range(len(rows)):
            # removes white spaces
            cols = list(filter(None, rows[y].split('\\')))
            for x in range(len(cols)):
                # Windows users may need to replace '\r\n'
                place = cols[x].replace('\n', '')

                self.world[(x, y)] = Unknown if place == '' else getattr(
                    __import__('Places'), place)(x, y)

    def getPlace(x, y):
        return PlanetX.world.get((x, y))
