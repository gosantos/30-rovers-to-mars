class Position:
    def __init__(self, x, y, direction):
        ''' Position object constructor

        :param x: the current position on the x coordinate (an integer)
        :param y: the current position on the y coordinate (an integet)
        :param direction: a direction represented by a character (n/w/s/e)
        :returns: a Position object
        '''
        self.x = x
        self.y = y
        self.direction = direction

    @staticmethod
    def from_string(str_position):
        ''' Constructs a new Position object from a string

        :param str_position: a string object formatted as: 'int int char'
        :returns: a Position object
        '''
        x, y, direction = str_position.split(' ')
        x, y = int(x), int(y)
        direction = str.lower(direction)
        return Position(x, y, direction)
