from plateau import Plateau
from position import Position
from rover import RoverCommand


class Parser:
    @staticmethod
    def read_input():
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
        return [RoverCommand(str.lower(command)) for command in str_commands]
