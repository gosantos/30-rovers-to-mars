class Plateau:
    ''' A Plateau object with x and y values specifying its size '''

    def __init__(self, x, y):
        ''' Plateau object constructor

        :param x: the current position on the x coordinate (an integer)
        :param y: the current position on the y coordinate (an integet)
        :returns: a Plateau object
        '''
        self.x = x
        self.y = y

    @staticmethod
    def from_string(str_plateau):
        ''' Constructs a new Plateau object from a string

        :param str_plateau: a string object formatted as: 'int int'
        :returns: a Plateau object
        '''
        x, y = str_plateau.split(' ')
        x, y = int(x), int(y)
        return Plateau(x, y)