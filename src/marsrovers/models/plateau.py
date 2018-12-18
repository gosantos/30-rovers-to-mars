X_AXIS = 0
Y_AXIS = 1


class Plateau:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_valid_position(self, position):
        return 0 <= position.x <= self.x and 0 <= position.y <= self.y


class PlateauFactory:
    @staticmethod
    def create(plateau):
        return Plateau(plateau[X_AXIS], plateau[Y_AXIS])
