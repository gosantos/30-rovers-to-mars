from .plateau import Plateau
from .position import Position
from .rover import RoverCommand


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
        return [RoverCommand(str.lower(command)) for command in str_commands]
