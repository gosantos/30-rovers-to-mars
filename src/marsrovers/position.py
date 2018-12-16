
class Position:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def __eq__(self, other):
        return type(other) is Position and self.__dict__ == other.__dict__

    @staticmethod
    def from_string(str_position):
        x, y, direction = str_position.split(' ')
        x, y = int(x), int(y)
        direction = str.lower(direction)
        return Position(x, y, direction)
