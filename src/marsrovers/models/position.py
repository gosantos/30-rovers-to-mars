X_AXIS = 0
Y_AXIS = 1
DIRECTION = 2


class Position:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction


class PositionFactory:
    @staticmethod
    def create(position):
        return Position(position[X_AXIS], position[Y_AXIS], position[DIRECTION])
