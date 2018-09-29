from enum import Enum, unique
from .plateau import Plateau
from .position import Position, Direction


@unique
class RoverCommand(Enum):
    MOVE_FORWARD = 'm'
    ROTATE_LEFT = 'l'
    ROTATE_RIGHT = 'r'


class Rover:
    ''' A Rover object able to rotate and move forward '''

    def __init__(self, plateau, position):
        ''' Rover object constructor

        :param plateau: a Plateau object
        :param position: a Position object
        :returns: a Rover object
        '''
        self._plateau = plateau
        self.position = position

        self.__left_rotations = {
            Direction.NORTH: Direction.WEST,
            Direction.WEST: Direction.SOUTH,
            Direction.SOUTH: Direction.EAST,
            Direction.EAST: Direction.NORTH,
        }

        self.__right_rotations = {
            Direction.NORTH: Direction.EAST,
            Direction.EAST: Direction.SOUTH,
            Direction.SOUTH: Direction.WEST,
            Direction.WEST: Direction.NORTH,
        }

        self.__commands = {
            RoverCommand.MOVE_FORWARD: self.move_forward,
            RoverCommand.ROTATE_LEFT: self.rotate_left,
            RoverCommand.ROTATE_RIGHT: self.rotate_right,
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
        print('({}, {}) - moving forward...'.format(self.position.x, 
                                                    self.position.y))
        newposition = None
        # here is the alternative version to the dictionary approach
        # I think this is the better choice for this case
        # since using a dictionary would actually create 4 new Position objects

        # with if/else statements we have more clutter, 
        # but we only create 1 object
        if self.position.direction == Direction.NORTH:
            newposition = Position(self.position.x, self.position.y + 1, self.position.direction)

        elif self.position.direction == Direction.SOUTH:
            newposition = Position(self.position.x, self.position.y - 1, self.position.direction)

        elif self.position.direction == Direction.EAST:
            newposition = Position(self.position.x + 1, self.position.y, self.position.direction)   

        elif self.position.direction == Direction.WEST:
            newposition = Position(self.position.x - 1, self.position.y, self.position.direction)

        if Rover.isValidPosition(self._plateau, newposition):
            self.position = newposition
            return self
        else:
            raise RuntimeError('Invalid move:', command)

        # raise unexpected error in case we get no matches at all
        raise RuntimeError('Unexpected error!')

    def rotate_left(self):
        ''' Rotates the Rover left, given its current direction '''
        print('({}, {}) - rotating left...'.format(self.position.x, 
                                                   self.position.y))
        # instead of doing a huge if/else (since python doesn't offer switch statements)
        # we use a dictionary to match the current direction (key) to a new direction (value)
        self.position.direction = self.__left_rotations[self.position.direction]
        return self

    def rotate_right(self):
        ''' Rotates the Rover right, given its current direction '''
        print('({}, {}) - rotating right...'.format(self.position.x, 
                                                    self.position.y))
        # instead of doing a huge if/else (since python doesn't offer switch statements)
        # we use a dictionary to match the current direction (key) to a new direction (value)
        self.position.direction = self.__right_rotations[self.position.direction]
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
