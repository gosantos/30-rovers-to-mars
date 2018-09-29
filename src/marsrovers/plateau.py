from .position import Position


class Plateau:
    ''' A Plateau object with x and y values specifying its size '''

    def __init__(self, x, y):
        ''' Plateau object constructor

        :param x: the current position on the x coordinate (an integer)
        :param y: the current position on the y coordinate (an integet)
        :returns: a Plateau object
        '''
        assert(type(x) is int and x >= 0)
        assert(type(y) is int and y >= 0)

        self.x = x
        self.y = y

    def __eq__(self, other):
        ''' Compares instance with another instance by attribute values 

        :param other: the object to be compared to
        :returns: a boolean specifying whether the other object is equal to this instance'''
        return type(other) is Plateau and self.__dict__ == other.__dict__

    @staticmethod
    def from_string(str_plateau):
        ''' Constructs a new Plateau object from a string

        :param str_plateau: a string object formatted as: 'int int'
        :returns: a Plateau object
        '''
        x, y = str_plateau.split(' ')
        x, y = int(x), int(y)
        return Plateau(x, y)
    
    def isValidPosition(self, position):
        ''' Checks whether the a position is valid or not, given the size of the plateau 

        :param plateau: a Plateau object
        :param position: a Position object
        :returns: a boolean that specifies whether the position is valid or not
        '''
        if position.x < 0 or position.x > self.x:
            return False
        if position.y < 0 or position.y > self.y:
            return False

        return True
