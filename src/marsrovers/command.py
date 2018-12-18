from src.marsrovers.models.position import Position
from .enums.commands import Commands, Directions


class Command:
    def match(self, command):
        raise Exception("Abstract class, implement it!")

    def move(self, position):
        raise Exception("Abstract class, implement it!")


class NorthCommand(Command):
    def match(self, command):
        return command == Directions.NORTH

    def move(self, position):
        return Position(position.x, position.y + 1, position.direction)


class SouthCommand(Command):
    def match(self, command):
        return command == Directions.SOUTH

    def move(self, position):
        return Position(position.x - 1, position.y, position.direction)


class EastCommand(Command):
    def match(self, command):
        return command == Directions.EAST

    def move(self, position):
        return Position(position.x + 1, position.y, position.direction)


class WestCommand(Command):
    def match(self, command):
        return command == Directions.WEST

    def move(self, position):
        return Position(position.x - 1, position.y, position.direction)


class RotateRightCommand(Command):
    def match(self, command):
        return command == Commands.RIGHT

    def move(self, position):
        right_rotations = {
            Directions.NORTH: Directions.EAST,
            Directions.EAST: Directions.SOUTH,
            Directions.SOUTH: Directions.WEST,
            Directions.WEST: Directions.NORTH,
        }

        return Position(position.x, position.y, right_rotations[position.direction])


class RotateLeftCommand(Command):
    def match(self, command):
        return command == Commands.LEFT

    def move(self, position):
        left_rotations = {
            Directions.NORTH: Directions.WEST,
            Directions.WEST: Directions.SOUTH,
            Directions.SOUTH: Directions.EAST,
            Directions.EAST: Directions.NORTH,
        }

        return Position(position.x, position.y, left_rotations[position.direction])


class CommandNotFound(Command):
    def match(self, command):
        return True

    def move(self, position):
        raise Exception("CommandNotFound exception")
