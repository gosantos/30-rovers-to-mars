

class Rover:
    ''' A Rover object able to rotate and move forward '''
    
    def __init__(self, plateau, position):
        ''' Rover object constructor

        :param plateau: a Plateau object
        :param position: a Position object
        :returns: a Rover object
        '''
        self._plateau = plateau
        self._position = position

        self.__left_rotations = {
            'n': 'w',
            'w': 's',
            's': 'e',
            'e': 'n',
        }

        self.__right_rotations = {
            'n': 'e',
            'w': 'n',
            's': 'w',
            'e': 's',
        }

        self.__commands = {
            'm': self.move_forward,
            'l': self.rotate_left,
            'r': self.rotate_right,
        }

    def execute(self, command):
        ''' Match a given command (within the available commands)
            and execute it
        '''
        self.__commands[command]()
        return self

    def move_forward(self):
        ''' Moves the Rover forward, given its current
            position and direction
        
        :raises: A RuntimeError in case of invalid direction value (no matches).
        :raises: A RuntimeError if the move is invalid.
        '''
        print('({}, {}) - moving forward...'.format(self._position.x, 
                                                    self._position.y))

        # here is the alternative version to the dictionary approach
        # I think this is the better choice for this case
        # since using a dictionary would actually create 4 new Position objects

        # with if/else statements we have more clutter, 
        # but we only create 1 object
        if self._position.direction == 'n':
            new_position = Position(self._position.x, self._position.y + 1, self._position.direction)

        elif self._position.direction == 's':
            new_position = Position(self._position.x, self._position.y - 1, self._position.direction)

        elif self._position.direction == 'e':
            new_position = Position(self._position.x + 1, self._position.y, self._position.direction)   

        elif self._position.direction == 'w':
            new_position = Position(self._position.x - 1, self._position.y, self._position.direction)
        
        if Rover.isValidPosition(self._plateau, new_position):
            self._position = new_position
            return self
        else:
            raise RuntimeError('Invalid move:', command)

        # raise unexpected error in case we get no matches at all
        raise RuntimeError('Unexpected error!')

    def rotate_left(self):
        ''' Rotates the Rover left, given its current direction '''
        print('({}, {}) - rotating left...'.format(self._position.x, 
                                                   self._position.y))
        # instead of doing a huge if/else (since python doesn't offer switch statements)
        # we use a dictionary to match the current direction (key) to a new direction (value)
        self._position.direction = self.__left_rotations[self._position.direction]
        return self

    def rotate_right(self):
        ''' Rotates the Rover right, given its current direction '''
        print('({}, {}) - rotating right...'.format(self._position.x, 
                                                    self._position.y))
        # instead of doing a huge if/else (since python doesn't offer switch statements)
        # we use a dictionary to match the current direction (key) to a new direction (value)
        self._position.direction = self.__right_rotations[self._position.direction]
        return self

    @staticmethod
    def isValidPosition(plateau, position):
        ''' Checks whether the a position is valid or not, given the size of the plateau 

        :param plateau: a Plateau object
        :param position: a Position object
        :returns: a boolean that specifies whether the position is valid or not
        '''
        if position.x < 0 or position.x > plateau.x:
            return False
        if position.y < 0 or position.y > plateau.y:
            return False

        return True


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


class Parser:
    @staticmethod
    def read_input():
        ''' Reads the input yielding Rover data

        :yields: a Plateau object, 
                 a Position object, 
                 and a list commands (as a list of characters)
        '''
        try:
            plateau = Plateau.from_string(input())

            while True:
                rover_position = Position.from_string(input())
                commands = Parser.parse_commands(input())
                yield plateau, rover_position, commands
        except EOFError as err:
            return


    @staticmethod
    def parse_commands(str_commands):
        ''' Parse a list of commands (as a list of characters)

        :returns: a list of lowercase characters
        '''
        return [str.lower(command) for command in str_commands]


if __name__ == '__main__':
    for (plateau, rover_position, commands) in Parser.read_input():
        print(plateau, rover_position, commands)
        rover = Rover(plateau, rover_position)
        for command in commands:
            rover.execute(command)
        print(rover._position.x, rover._position.y, rover._position.direction)  