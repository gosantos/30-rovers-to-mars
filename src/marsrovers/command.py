from .position import Position
from .enums.directions import Commands


class Command:
    def match(self, command):
        raise Exception("Abstract class, implement it!")

    def move(self, position):
        raise Exception("Abstract class, implement it!")


class NorthCommand(Command):
    def match(self, command):
        return command == Commands.NORTH

    def move(self, position):
        return Position(position.x, position.y + 1, position.direction)


class SouthCommand(Command):
    def match(self, command):
        return command == Commands.SOUTH

    def move(self, position):
        return Position(position.x + 1, position.y, position.direction)


class EastCommand(Command):
    def match(self, command):
        return command == Commands.EAST

    def move(self, position):
        return Position(position.x + 1, position.y, position.direction)


class WestCommand(Command):
    def match(self, command):
        return command == Commands.WEST

    def move(self, position):
        return Position(position.x - 1, position.y, position.direction)


class RotateRightCommand(Command):
    def match(self, command):
        return command == Commands.RIGHT

    def move(self, position):
        right_rotations = {
            Commands.NORTH: Commands.EAST,
            Commands.EAST: Commands.SOUTH,
            Commands.SOUTH: Commands.WEST,
            Commands.WEST: Commands.NORTH,
        }

        return Position(position.x, position.y, right_rotations[position.direction])


class RotateLeftCommand(Command):
    def match(self, command):
        return command == Commands.LEFT

    def move(self, position):
        left_rotations = {
            Commands.NORTH: Commands.WEST,
            Commands.WEST: Commands.SOUTH,
            Commands.SOUTH: Commands.EAST,
            Commands.EAST: Commands.NORTH,
        }

        return Position(position.x, position.y, left_rotations[position.direction])


class CommandNotFound(Command):
    def match(self, command):
        return True

    def move(self, position):
        raise Exception("CommandNotFound exception")
